import time
import random
import json
import google.generativeai as genai
from fastapi import HTTPException
from config import Config

class GeminiService:
    def __init__(self):
        self.last_api_call = 0
        self.minimum_wait = 7
        self.setup_gemini()

    def setup_gemini(self):
        try:
            genai.configure(api_key=Config.API_KEY)
            model = genai.GenerativeModel(
                model_name=Config.MODEL_NAME,
                generation_config=Config.get_generation_config(),
                safety_settings=Config.get_safety_settings(),
            )
            self.gemini_chat = model.start_chat(history=[])
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Gemini API error: {str(e)}")

    async def call_api(self, prompt: str, max_retries: int = 5):
        for attempt in range(max_retries):
            try:
                current_time = time.time()
                elapsed = current_time - self.last_api_call
                if elapsed < self.minimum_wait:
                    time.sleep(self.minimum_wait - elapsed)
                self.last_api_call = time.time()

                response = self.gemini_chat.send_message(prompt)
                return response.text.strip()
            except Exception as e:
                if attempt == max_retries - 1:
                    raise HTTPException(status_code=500, detail=f"API call failed: {str(e)}")
                wait_time = (2 ** attempt) + random.random()
                time.sleep(wait_time)
