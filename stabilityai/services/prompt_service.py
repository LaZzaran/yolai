import json
from stabilityai.config import MODEL_NAME
from model_runner import run_model
import google.generativeai as genai

def create_structured_prompt(text):
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

def get_presentation_content(text):
    generation_config = {"temperature": 0.7,
                         "top_p": 0.95,
                         "top_k": 40,
                         "max_output_tokens": 8192}
    model = genai.GenerativeModel(model_name=MODEL_NAME, generation_config=generation_config)
    prompt = create_structured_prompt(text)
    response = model.generate_content(prompt)

    try:
        content = json.loads(response.text)
        for slide in content['slides']:
            if 'image_keyword' in slide:
                search_term = slide['image_keyword']['search_term']
                search_term += " high quality educational"
                slide['image_keyword']['search_term'] = search_term
        return content
    except json.JSONDecodeError:
        cleaned_response = response.text.strip()
        cleaned_response = cleaned_response[cleaned_response.find('{'):cleaned_response.rfind('}') + 1]
        return json.loads(cleaned_response)
