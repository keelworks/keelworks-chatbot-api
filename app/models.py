from datetime import datetime
from sqlalchemy import String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# SQLAlchemy model representing the 'unanswered_questions' table in the database
class UnansweredQuestion(Base):
    __tablename__ = 'unanswered_questions'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    question: Mapped[str] = mapped_column(String(255))

    def __repr__(self) -> str:
        return f'UnansweredQuestion(id={self.id!r}, question={self.question!r}, created_at={self.created_at!r})'
    