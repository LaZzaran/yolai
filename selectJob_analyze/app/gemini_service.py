import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold, GenerationConfig
from fastapi import HTTPException
from app.questions import Questions
from typing import Dict
class GeminiService:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.setup_complete = False
        self.setup()

    def setup(self):
        try:
            genai.configure(api_key=self.api_key)
            generation_config = GenerationConfig(
                temperature=0.45,
                top_p=0.85,
                top_k=40,
                max_output_tokens=8192,
            )

            self.model = genai.GenerativeModel(
                model_name='gemini-1.5-pro',
                generation_config=generation_config,
                safety_settings={
                    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
                    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
                    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
                }
            )
            self.chat = self.model.start_chat(history=[])
            self.setup_complete = True
        except Exception as e:
            raise RuntimeError(f"Failed to setup Gemini: {str(e)}")

    def get_analysis_prompt(self, answers: Dict[int, str]) -> str:
        analysis_text = "KİŞİ ANALİZİ:\n\n"
        for q_idx, answer in answers.items():
            if q_idx >= Questions.total_questions():
                raise ValueError(f"Invalid question index: {q_idx}")
            analysis_text += f"Soru: {Questions.get_question(q_idx)}\n"
            analysis_text += f"Cevap: {answer}\n\n"

        return f"""
        Aşağıda bir kişinin kariyer danışmanlığı için verdiği cevaplar var.
        Bu bilgilere dayanarak kişiye en uygun 5 meslek önerisi yap.
        Kişinin yaşını, ilgi alanlarını, eğitim durumunu ve beklentilerini dikkate al.

        {analysis_text}

        Lütfen şu formatta cevap ver:

        GENEL DEĞERLENDİRME:
        [Kişinin verdiği cevaplara göre genel profili ve öne çıkan özelliklerinin detaylı analizi]

        ÖNERİLEN MESLEKLER:
        1. [Meslek Adı]
           - Neden uygun: [Detaylı açıklama]
           - Gerekli eğitim/sertifikalar: [Eğitim gereksinimleri]
           - Kariyer yolu: [İlerleme imkanları]

        2. [Meslek Adı]
           - Neden uygun: [Detaylı açıklama]
           - Gerekli eğitim/sertifikalar: [Eğitim gereksinimleri]
           - Kariyer yolu: [İlerleme imkanları]

        3. [Meslek Adı]
           - Neden uygun: [Detaylı açıklama]
           - Gerekli eğitim/sertifikalar: [Eğitim gereksinimleri]
           - Kariyer yolu: [İlerleme imkanları]

        4. [Meslek Adı]
           - Neden uygun: [Detaylı açıklama]
           - Gerekli eğitim/sertifikalar: [Eğitim gereksinimleri]
           - Kariyer yolu: [İlerleme imkanları]

        5. [Meslek Adı]
           - Neden uygun: [Detaylı açıklama]
           - Gerekli eğitim/sertifikalar: [Eğitim gereksinimleri]
           - Kariyer yolu: [İlerleme imkanları]

        EK ÖNERİLER:
        [Kişiye özel tavsiyeler, gelişim önerileri ve dikkat etmesi gereken noktalar]
        """

    async def analyze_answers(self, answers: Dict[int, str]) -> str:
        if not self.setup_complete:
            raise RuntimeError("Gemini setup not completed")

        try:
            prompt = self.get_analysis_prompt(answers)
            response = self.chat.send_message(prompt)
            return response.text.strip()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")
