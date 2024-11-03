from google.generativeai.types import HarmCategory, HarmBlockThreshold
from google.generativeai.types import GenerationConfig


class Config:
    API_KEY = "YOUR_APİ_KEY"
    MODEL_NAME = "gemini-1.5-pro"

    @staticmethod
    def get_generation_config():
        return GenerationConfig(
            temperature=0.45,
            top_p=0.85,
            top_k=40,
            max_output_tokens=8192,
        )

    @staticmethod
    def get_safety_settings():
        return {
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        }