import { useChat } from "ai/react";
import InteractiveAvatar from "./InteractiveAvatar";

export function AIChatBox({ isVideoVisible }: { isVideoVisible: boolean }) {
  const { messages } = useChat();

  return (
    <div className="w-full h-full flex flex-col">
      {isVideoVisible && <InteractiveAvatar />}
    </div>
  );
}
