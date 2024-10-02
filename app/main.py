from typing import Dict
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from . import settings, database, chatbot, schemas, crud

app = FastAPI()

# Apply CORS middleware settings
settings.add_cors_middleware(app)

# Get initial start up message
@app.get("/api/")
async def home() -> Dict[str, str]:
    return {'message': "Ahoy! I’m Captain Keel, here to navigate all your questions about Keelworks. Ask away, and let’s set sail toward the answers you seek!"}

# Post a question if threshold is below limit otherwise returns the answer of the best matching question
@app.post("/api/ask")
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
            "Hmm, looks like we’ve sailed into uncharted waters! I don’t have an answer for that right now, but I’ll hoist the sails and work on it. In the meantime, try adjusting your course with a new question!"
        )
        response = schemas.UnansweredQuestion.model_validate(created_question)
    
    return response
