from pydantic import BaseModel
from typing import Dict, List, Any

class SinavCevap(BaseModel):
    cevaplar: Dict[int, str]

class SoruModel(BaseModel):
    question: str
    options: List[str]
    correct_answer: str
    explanation: str

class SinavVerisi(BaseModel):
    questions: List[SoruModel]