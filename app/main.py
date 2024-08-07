from fastapi import FastAPI
from pydantic import BaseModel
from .model import get_best_answer

app = FastAPI()

class Query(BaseModel):
    query: str

@app.get('/')
def home():
    return {'message': 'Welcome to the KeelWorks Chatbot. Ask me anything about KeelWorks!'}

@app.post('/ask')
def ask_question(query: Query):
    user_query = query.query
    answer, is_above_threshold = get_best_answer(user_query)

    if is_above_threshold:
        return {'question': user_query, 'answer': answer}
    else:
        # save question in database
        return {'question': user_query, 'answer': "Sorry, I don't have the answer for that right now."}

# To start the server:
# uvicorn app.main:app --host 0.0.0.0 --port 80

# Before running server:
# 1. Make sure there is a chatbot_model pickle file in model/: 'python -m scripts.save_model'