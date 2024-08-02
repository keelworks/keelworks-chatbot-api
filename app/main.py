from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Query(BaseModel):
    query: str

@app.get("/")
def home():
    return {"message": "Welcome to the KeelWorks Chatbot. Ask me anything about KeelWorks!"}

@app.post("/ask")
def ask_question(query: Query):
    user_query = query.query
    answer = "This is a placeholder response."
    return {"question": user_query, "answer": answer}
