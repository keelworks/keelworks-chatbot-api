from pydantic import BaseModel
from datetime import datetime

class UnansweredQuestionBase(BaseModel):
    question: str

class UnansweredQuestionCreate(UnansweredQuestionBase):
    pass

class UnansweredQuestion(UnansweredQuestionBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True