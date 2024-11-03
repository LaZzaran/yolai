import requests
from config.settings import Settings

class AudioService:
    def __init__(self):
        self.api_key = Settings.XI_API_KEY
        self.voice_id = Settings.VOICE_ID
        self.chunk_size = Settings.CHUNK_SIZE

    def generate_audio(self, text: str, output_path: str) -> bool:
        if not self.api_key or self.api_key == 'your_eleven_labs_key_here':
            print("Eleven Labs API anahtarı ayarlanmamış. Ses oluşturma atlanıyor.")
            return False

        tts_url = f"https://api.elevenlabs.io/v1/text-to-speech/{self.voice_id}/stream"

        headers = {
            "Accept": "application/json",
            "xi-api-key": self.api_key
        }

        data = {
            "text": text,
            "model_id": "eleven_multilingual_v2",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.8,
                "style": 0.0,
                "use_speaker_boost": True,
                "language": "tr"
            }
        }

        try:
            response = requests.post(tts_url, headers=headers, json=data, stream=True)
            response.raise_for_status()

            with open(output_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=self.chunk_size):
                    f.write(chunk)
            return True
        except Exception as e:
            print(f"Ses oluşturma hatası: {str(e)}")
            return False
