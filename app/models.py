from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from .database import Base

class UnansweredQuestion(Base):
    __tablename__ = 'unanswered_questions'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    question: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    def __repr__(self) -> str:
        return f"UnansweredQuestion(id={self.id!r}, question={self.question!r}, created_at={self.created_at!r})"