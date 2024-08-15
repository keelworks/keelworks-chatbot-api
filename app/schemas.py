from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Query(BaseModel):
    query: str

class UnansweredQuestionCreate(BaseModel):
    question: str

class UnansweredQuestion(BaseModel):
    id: Optional[int] = None
    created_at: Optional[datetime] = None
    question: str
    answer: Optional[str] = None

    class Config:
        from_attributes = True