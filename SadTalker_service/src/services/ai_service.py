import google.generativeai as genai
from config.settings import Settings

class AIService:
    def __init__(self):
        genai.configure(api_key=Settings.GOOGLE_API_KEY)
        self.model = genai.GenerativeModel('gemini-1.5-pro')

    def create_structured_prompt(self, text: str) -> str:
        return f"""
        Lütfen aşağıdaki metinden profesyonel bir sunum oluştur. Her slayt için, slaytın içeriğini en iyi temsil edecek bir tablo dışı görsel arama terimi belirle.
        JSON formatında yanıt ver.

        Metin: {text}

        Yanıtı aşağıdaki JSON formatında ver:
        {{
            "slides": [
                {{
                    "title": "Başlık",
                    "points": [
                        "Madde 1",
                        "Madde 2",
                        "Madde 3"
                    ],
                    "image_keyword": {{
                        "search_term": "Arama terimi",
                        "description": "Bu terimin seçilme nedeni"
                    }}
                }}
            ]
        }}

        Her slayt için image_keyword belirleme kuralları:
        1. Slaytın ana konusunu en iyi yansıtan bir terim seç
        2. Terimi Türkçe olarak belirt
        3. Tablo içeren görselleri dışla, tablo kullanma
        4. Görsel tipini belirt (diagram, illustration, photo, etc.)
        5. Bilimsel/akademik görseller için sonuna "scientific" veya "academic" ekle

        Sunum şunları içermeli:
        1. Kapak slaytı (başlık ve alt başlık)
        2. İçindekiler/Genel Bakış
        3-8. Ana içerik slaytları (her birinde 3-5 madde)
        9. Özet/Sonuç slaytı
        """

    def generate_content(self, text: str):
        prompt = self.create_structured_prompt(text)
        return self.model.generate_content(prompt)
