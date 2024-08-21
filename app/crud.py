from sqlalchemy.ext.asyncio import AsyncSession
from . import models, schemas

# Create a new unanswered question in database via POST
async def create_unanswered_question(
    db: AsyncSession, 
    user_question: schemas.UnansweredQuestionCreate
) -> models.UnansweredQuestion:
    db_question = models.UnansweredQuestion(question=user_question.user_question)
    db.add(db_question)
    await db.commit()
    await db.refresh(db_question)
    return db_question
