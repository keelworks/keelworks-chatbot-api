from sqlalchemy.ext.asyncio import AsyncSession
from . import models, schemas

# Method for creating a new unanswered question in database
async def create_unanswered_question(db: AsyncSession, question: schemas.UnansweredQuestionCreate):
    db_question = models.UnansweredQuestion(question=question.question)
    db.add(db_question)
    await db.commit()
    await db.refresh(db_question)
    return db_question