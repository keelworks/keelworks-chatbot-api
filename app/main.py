from typing import Dict
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from . import settings, database, chatbot, schemas, crud

app = FastAPI()

# Apply CORS middleware settings
settings.add_cors_middleware(app)

# Get initial start up message
@app.get('/')
async def home() -> Dict[str, str]:
    return {'message': "Hi, I'm KeelBot. Ask me anything about KeelWorks!"}

# Post a question if threshold is below limit otherwise returns the answer of the best matching question
@app.post('/ask')
async def ask_question(
    user_question: schemas.UnansweredQuestionCreate, 
    db: AsyncSession = Depends(database.get_session)
) -> schemas.UnansweredQuestion:
    user_query = user_question.user_question.strip()

    answer, is_above_threshold = chatbot.get_best_answer(user_query)

    if is_above_threshold:
        response = schemas.UnansweredQuestion(question=user_query, answer=answer, id=None, created_at=None)
    else:
        created_question = await crud.create_unanswered_question(db, user_question=schemas.UnansweredQuestionCreate(user_question=user_query))
        created_question.answer = (
            "I'm sorry, I don’t have an answer for that right now. "
            "I’ll add your question to our list of 'Unanswered Questions' and work on getting you an answer soon! "
            "In the meantime, feel free to ask another question or rephrase your query."
        )
        response = schemas.UnansweredQuestion.model_validate(created_question)
    
    return response
