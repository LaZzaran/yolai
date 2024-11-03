from typing import Dict, Any
import json
from fastapi import HTTPException
from .gemini_service import GeminiService
from models import SinavVerisi, SinavCevap

class QuizService:
    def __init__(self):
        self.gemini_service = GeminiService()
        self.quiz_data = None

    async def create_quiz(self, content: str, question_count: int = 10) -> Dict[str, Any]:
        try:
            prompt = f"""
            Aşağıdaki içerikten {question_count} adet çoktan seçmeli soru oluştur ve cevapları TAM OLARAK bu JSON formatında ver:
            {{
                "questions": [
                    {{
                        "question": "soru metni",
                        "options": ["A) seçenek", "B) seçenek", "C) seçenek", "D) seçenek"],
                        "correct_answer": "A",
                        "explanation": "Doğru cevabın kısa açıklaması"
                    }}
                ]
            }}
            Her sorunun doğru cevabı farklı bir cevap olsun!!
            İçerik:
            {content}
            """

            response = await self.gemini_service.call_api(prompt)
            start = response.find('{')
            end = response.rfind('}') + 1

            if start == -1 or end == 0:
                raise ValueError("Valid JSON not found")

            self.quiz_data = json.loads(response[start:end])
            return self.quiz_data

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Quiz creation error: {str(e)}")

    def grade_quiz(self, quiz_answers: SinavCevap) -> Dict[str, Any]:
        if not self.quiz_data:
            raise HTTPException(status_code=400, detail="No current quiz data available")

        results = []
        correct = 0
        total = len(self.quiz_data["questions"])

        for i, question in enumerate(self.quiz_data["questions"], 1):
            user_answer = quiz_answers.cevaplar.get(i)
            is_correct = user_answer == question["correct_answer"]

            if is_correct:
                correct += 1

            results.append({
                "soru_numarasi": i,
                "dogru_mu": is_correct,
                "dogru_cevap": question["correct_answer"],
                "aciklama": question["explanation"]
            })

        return {
            "toplam_soru": total,
            "dogru_cevaplar": correct,
            "yanlis_cevaplar": total - correct,
            "basari_orani": (correct / total) * 100,
            "detayli_sonuclar": results
        }