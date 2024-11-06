import type { StartAvatarResponse } from "@heygen/streaming-avatar";
import StreamingAvatar, {
  AvatarQuality,
  StreamingEvents,
  VoiceEmotion,
} from "@heygen/streaming-avatar";
import { Button } from "@nextui-org/react";
import { Clock, Brain, Robot, Microphone } from "@phosphor-icons/react";
import { useEffect, useRef, useState, useCallback, useReducer } from "react";
import { AVATARS } from "@/app/lib/constants";
import { saveAs } from 'file-saver';

type ConversationAction = 
  | { type: 'ADD_MESSAGE'; payload: string }
  | { type: 'CLEAR' };

function conversationReducer(state: string[], action: ConversationAction): string[] {
  switch (action.type) {
    case 'ADD_MESSAGE':
      return [...state, action.payload];
    case 'CLEAR':
      return [];
    default:
      return state;
  }
}

export default function InteractiveAvatar() {
  const [isLoadingSession, setIsLoadingSession] = useState(false);
  const [stream, setStream] = useState<MediaStream>();
  const [debug, setDebug] = useState<string>();
  const [data, setData] = useState<StartAvatarResponse>();
  const videoRef = useRef<HTMLVideoElement>(null);
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const avatar = useRef<StreamingAvatar | null>(null);
  const [isUserTalking, setIsUserTalking] = useState(false);
  const [timeLeft, setTimeLeft] = useState(300); // 5 minutes in seconds
  const [isSessionActive, setIsSessionActive] = useState(false);
  const [conversation, dispatchConversation] = useReducer(conversationReducer, []);
  const conversationRef = useRef<string[]>([]);
  const [isWebSocketClosed, setIsWebSocketClosed] = useState(false);
  const [isSessionEnded, setIsSessionEnded] = useState(false);
  const [isMuted, setIsMuted] = useState(false);
  const [isRecording, setIsRecording] = useState(false);
  const [audioChunks, setAudioChunks] = useState<Blob[]>([]);
  const mediaRecorderRef = useRef<MediaRecorder | null>(null);

  const addToConversation = useCallback((message: string) => {
    dispatchConversation({ type: 'ADD_MESSAGE', payload: message });
    conversationRef.current = [...conversationRef.current, message];
    console.log("Updated conversation:", conversationRef.current);
  }, []);

  useEffect(() => {
    let timer: NodeJS.Timeout;
    if (isSessionActive) {
      timer = setInterval(() => {
        setTimeLeft((prev) => {
          if (prev <= 1) {
            clearInterval(timer);
            endSession();
            return 0;
          }
          return prev - 1;
        });
      }, 1000);
    }
    return () => clearInterval(timer);
  }, [isSessionActive]);

  async function fetchAccessToken() {
    try {
      const response = await fetch("/api/get-access-token", {
        method: "POST",
      });
      const token = await response.text();
      console.log("Access Token:", token);
      return token;
    } catch (error) {
      console.error("Error fetching access token:", error);
      setDebug(`Error fetching access token: ${error}`);
    }
    return "";
  }

  async function startSession() {
    setIsLoadingSession(true);
    setDebug("Starting session...");
    setIsSessionEnded(false);
    dispatchConversation({ type: 'CLEAR' });
    conversationRef.current = [];
    const newToken = await fetchAccessToken();

    if (!newToken) {
      setDebug("Failed to fetch access token");
      setIsLoadingSession(false);
      return;
    }

    // Start audio recording
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      mediaRecorderRef.current = new MediaRecorder(stream);
      mediaRecorderRef.current.ondataavailable = (event) => {
        if (event.data.size > 0) {
          setAudioChunks((chunks) => [...chunks, event.data]);
        }
      };
      mediaRecorderRef.current.start();
      setIsRecording(true);
    } catch (error) {
      console.error("Error starting audio recording:", error);
      setDebug(`Error starting audio recording: ${error}`);
    }

    avatar.current = new StreamingAvatar({
      token: newToken,
    });

    avatar.current.on(StreamingEvents.AVATAR_START_TALKING, (e) => {
      console.log("Avatar started talking", e);
      setDebug("Avatar started talking");
      if (e.detail.text) {
        console.log("Adding avatar message to conversation:", e.detail.text);
        addToConversation(`Avatar: ${e.detail.text}`);
      }
    });
    avatar.current.on(StreamingEvents.AVATAR_STOP_TALKING, (e) => {
      console.log("Avatar stopped talking", e);
      setDebug("Avatar stopped talking");
    });
    avatar.current.on(StreamingEvents.STREAM_DISCONNECTED, () => {
      console.log("Stream disconnected");
      setDebug("Stream disconnected");
      setIsWebSocketClosed(true);
    });
    avatar.current?.on(StreamingEvents.STREAM_READY, (event) => {
      console.log(">>>>> Stream ready:", event.detail);
      setStream(event.detail);
      setDebug("Stream ready");
    });
    avatar.current?.on(StreamingEvents.USER_START, (event) => {
      console.log(">>>>> User started talking:", event);
      setIsUserTalking(true);
      setDebug("User started talking");
    });
    avatar.current?.on(StreamingEvents.USER_STOP, (event) => {
      console.log(">>>>> User stopped talking:", event);
      setIsUserTalking(false);
      setDebug("User stopped talking");
      if (event.detail.transcript) {
        console.log("Adding user message to conversation:", event.detail.transcript);
        addToConversation(`User: ${event.detail.transcript}`);
      }
    });

    try {
      const res = await avatar.current.createStartAvatar({
        quality: AvatarQuality.Low,
        avatarName: AVATARS[0].avatar_id, // Default to the first avatar
        knowledgeId: "",
        voice: {
          rate: 1.5,
          emotion: VoiceEmotion.EXCITED,
        },
        language: 'en',
      });

      console.log("Avatar session created:", res);
      setData(res);
      setDebug("Avatar session created");
      await avatar.current?.startVoiceChat();
      console.log("Voice chat started");
      setDebug("Voice chat started");
      setIsSessionActive(true);
    } catch (error) {
      console.error("Error starting avatar session:", error);
      setDebug(`Error starting avatar session: ${error}`);
    } finally {
      setIsLoadingSession(false);
    }
  }

  async function handleInterrupt() {
    if (!avatar.current) {
      setDebug("Avatar API not initialized");
      return;
    }
    await avatar.current
      .interrupt()
      .catch((e) => {
        setDebug(`Error interrupting: ${e.message}`);
      });
  }

  async function endSession() {
    if (avatar.current) {
      await avatar.current.stopAvatar();
    }
    setStream(undefined);
    setDebug("Session ended");
    setIsSessionActive(false);
    setTimeLeft(300); // Reset timer
    setIsSessionEnded(true);

    // Stop audio recording
    if (mediaRecorderRef.current && isRecording) {
      mediaRecorderRef.current.stop();
      setIsRecording(false);
    }

    console.log("Conversation at end of session:", conversationRef.current);

    if (conversationRef.current.length > 0) {
      const conversationText = conversationRef.current.join('\n');
      console.log("Conversation text to save:", conversationText);

      if (conversationText.trim()) {
        try {
          const blob = new Blob([conversationText], { type: 'text/plain;charset=utf-8' });
          saveAs(blob, 'interview_conversation.txt');
          console.log("File saved successfully");
        } catch (error) {
          console.error("Error saving file:", error);
        }
      } else {
        console.log("Conversation text is empty after trimming");
      }
    } else {
      console.log("Conversation array is empty");
    }

    setIsWebSocketClosed(false);
    setAudioChunks([]);
  }

  const toggleMute = useCallback(() => {
    setIsMuted(prev => !prev);
  }, []);

  useEffect(() => {
    if (!avatar.current) return;

    const handleAvatarStartTalking = (e: any) => {
      console.log("Avatar started talking", e);
      setDebug("Avatar started talking");
      if (e.detail.text) {
        console.log("Adding avatar message to conversation:", e.detail.text);
        addToConversation(`Avatar: ${e.detail.text}`);
      }
    };

    const handleUserStop = (event: any) => {
      console.log("User stopped talking", event);
      setIsUserTalking(false);
      setDebug("User stopped talking");
      if (event.detail.transcript) {
        console.log("Adding user message to conversation:", event.detail.transcript);
        addToConversation(`User: ${event.detail.transcript}`);
      }
    };

    const handleStreamDisconnected = () => {
      console.log("Stream disconnected");
      setDebug("Stream disconnected");
      setIsWebSocketClosed(true);
    };

    avatar.current.on(StreamingEvents.AVATAR_START_TALKING, handleAvatarStartTalking);
    avatar.current.on(StreamingEvents.USER_STOP, handleUserStop);
    avatar.current.on(StreamingEvents.STREAM_DISCONNECTED, handleStreamDisconnected);

    return () => {
      avatar.current?.off(StreamingEvents.AVATAR_START_TALKING, handleAvatarStartTalking);
      avatar.current?.off(StreamingEvents.USER_STOP, handleUserStop);
      avatar.current?.off(StreamingEvents.STREAM_DISCONNECTED, handleStreamDisconnected);
    };
  }, [avatar.current, addToConversation]);

  useEffect(() => {
    if (isWebSocketClosed && !isSessionEnded) {
      endSession();
    }
  }, [isWebSocketClosed, isSessionEnded]);

  useEffect(() => {
    if (stream && videoRef.current && canvasRef.current) {
      videoRef.current.srcObject = stream;
      const ctx = canvasRef.current.getContext('2d');
      
      const processFrame = () => {
        if (videoRef.current && ctx) {
          ctx.drawImage(videoRef.current, 0, 0, canvasRef.current!.width, canvasRef.current!.height);
          const imageData = ctx.getImageData(0, 0, canvasRef.current!.width, canvasRef.current!.height);
          const data = imageData.data;

          for (let i = 0; i < data.length; i += 4) {
            const r = data[i];
            const g = data[i + 1];
            const b = data[i + 2];

            // If it's green, make it transparent
            if (g > 100 && r < 100 && b < 100) {
              data[i + 3] = 0; // Alpha channel
            }
          }

          ctx.putImageData(imageData, 0, 0);
        }
        requestAnimationFrame(processFrame);
      };

      videoRef.current.onloadedmetadata = () => {
        videoRef.current!.play();
        processFrame();
      };
    }
  }, [stream]);

  useEffect(() => {
    console.log("Conversation state updated:", conversation);
  }, [conversation]);

  useEffect(() => {
    console.log("Avatar instance:", avatar.current);
    if (!avatar.current) return;
    // ... rest of the useEffect
  }, [avatar.current]);

  useEffect(() => {
    if (!isRecording && audioChunks.length > 0) {
      const audioBlob = new Blob(audioChunks, { type: 'audio/webm' });
      const audioUrl = URL.createObjectURL(audioBlob);
      const link = document.createElement('a');
      link.href = audioUrl;
      link.download = 'interview_audio.webm';
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }
  }, [isRecording, audioChunks]);

  return (
    <div className="w-full h-full flex flex-col justify-between bg-gradient-to-br from-blue-900 via-indigo-900 to-purple-900 p-2 md:p-4">
      {/* Timer with icons */}
      <div className="w-full flex items-center justify-between px-2 md:px-4 mb-2">
        <Brain size={16} weight="duotone" className="text-blue-300" />
        <div className="flex items-center space-x-2">
          <Clock size={16} weight="duotone" className="text-purple-300" />
          <div className="text-white text-sm md:text-lg font-bold">
            Kalan Süre: {Math.floor(timeLeft / 60)}:{timeLeft % 60 < 10 ? '0' : ''}{timeLeft % 60}
          </div>
        </div>
        <Robot size={16} weight="duotone" className="text-blue-300" />
      </div>

      {/* Avatar or Start Button */}
      <div className="flex-grow flex items-center justify-center w-full mb-2 md:mb-4">
        {stream ? (
          <div className="w-full h-full flex items-center justify-center">
            <video
              ref={videoRef}
              className="hidden"
              autoPlay
              playsInline
            />
            <canvas
              ref={canvasRef}
              className="w-full h-full object-contain"
              style={{
                maxWidth: '100%',
                maxHeight: 'calc(100vh - 140px)',
                aspectRatio: '16 / 9',
              }}
            />
          </div>
        ) : (
          <Button
            className="bg-indigo-500 hover:bg-indigo-600 text-white px-4 py-2 md:px-6 md:py-3 text-sm md:text-lg rounded-full shadow-lg"
            onClick={startSession}
          >
            Mülakat oturumunu başlat
          </Button>
        )}
      </div>

      {/* Controls */}
      <div className="w-full flex justify-center items-center gap-2 mt-2">
        <Button
          className="bg-blue-500 hover:bg-blue-600 text-white rounded-full text-xs md:text-base px-3 py-1 md:px-4 md:py-2"
          onClick={handleInterrupt}
        >
          Durdur
        </Button>
        <Button
          className="bg-purple-500 hover:bg-purple-600 text-white rounded-full text-xs md:text-base px-3 py-1 md:px-4 md:py-2"
          onClick={endSession}
        >
          Bitir
        </Button>
        <Button
          className="bg-indigo-500 hover:bg-indigo-600 text-white rounded-full text-xs md:text-base px-3 py-1 md:px-4 md:py-2"
          onClick={toggleMute}
        >
          {isMuted ? 'Aç' : 'Sustur'}
        </Button>
      </div>

      {/* Conversation display is removed as it's not in the provided image */}
    </div>
  );
}
