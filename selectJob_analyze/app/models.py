from pydantic import BaseModel
from typing import Dict

class Answer(BaseModel):
    answer: str

class SessionState(BaseModel):
    current_question: int = 0
    answers: Dict[int, str] = {}
    completed: bool = False