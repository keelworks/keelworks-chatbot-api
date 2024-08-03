from fastapi import FastAPI
from pydantic import BaseModel
from .model import get_best_answer, faqs, faq_embeddings

app = FastAPI()

class Query(BaseModel):
    query: str

@app.get("/")
def home():
    return {"message": "Welcome to the KeelWorks Chatbot. Ask me anything about KeelWorks!"}

@app.post("/ask")
def ask_question(query: Query):
    user_query = query.query
    answer = get_best_answer(user_query, faqs, faq_embeddings)
    return {"question": user_query, "answer": answer}

# To start the server:
# uvicorn app.main:app --host 0.0.0.0 --port 80

# Before running server, make sure there is a saved chatbot_model in model/
# To save a chatbot_model, run scripts/save_model.py