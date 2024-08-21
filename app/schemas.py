from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# User input model validations
class UnansweredQuestionCreate(BaseModel):
    user_question: str

# Instance of UnansweredQuestion model validations
class UnansweredQuestion(BaseModel):
    id: Optional[int] = None
    created_at: Optional[datetime] = None
    question: str
    answer: str

    class Config:
        from_attributes = True
        