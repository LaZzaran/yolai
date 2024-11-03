from fastapi import HTTPException
from models import Prompt
import google.generativeai as genai

class ContentGenerator:
    def __init__(self):
        self.generation_config = {
            "temperature": 0.7,
            "top_p": 0.9,
            "top_k": 40,
            "max_output_tokens": 8192,
        }
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-pro",
            generation_config=self.generation_config
        )

    def generate(self, text: str) -> str:
        prompt = Prompt.create(text)
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
