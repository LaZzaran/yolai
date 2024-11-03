from .models import SessionState
from .questions import Questions
from fastapi import HTTPException
from app.models import SessionState
from app.questions import Questions
class SessionManager:
    def __init__(self):
        self.session = SessionState()

    def get_current_question(self):
        if self.session.completed:
            return {"status": "completed", "message": "Tüm sorular tamamlandı"}

        if self.session.current_question >= Questions.total_questions():
            self.session.completed = True
            return {"status": "completed", "message": "Tüm sorular tamamlandı"}

        return {
            "question_number": self.session.current_question + 1,
            "total_questions": Questions.total_questions(),
            "question": Questions.get_question(self.session.current_question)
        }

    def submit_answer(self, answer: str):
        if self.session.completed:
            raise HTTPException(status_code=400, detail="Tüm sorular zaten tamamlandı")

        if not answer.strip():
            raise HTTPException(status_code=400, detail="Cevap boş olamaz")

        self.session.answers[self.session.current_question] = answer
        self.session.current_question += 1

        if self.session.current_question >= Questions.total_questions():
            self.session.completed = True
            return None

        return {
            "status": "success",
            "next_question_number": self.session.current_question + 1,
            "next_question": Questions.get_question(self.session.current_question),
            "progress": {
                "completed": self.session.current_question,
                "total": Questions.total_questions()
            }
        }

    def get_progress(self):
        return {
            "current_question": self.session.current_question,
            "total_questions": Questions.total_questions(),
            "completed_questions": len(self.session.answers),
            "progress_percentage": (len(self.session.answers) / Questions.total_questions()) * 100,
            "is_completed": self.session.completed
        }

    def reset(self):
        self.session = SessionState()

    def get_answers(self):
        return self.session.answers
