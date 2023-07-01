from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Chat(BaseModel):
    message: str


@app.get("/hi")
def hi():
    return {"reply": "hi"}


@app.post("/chat")
def chat(chat: Chat):
    message = chat.message
    return {"reply": "Message Received!" + message}


@app.post("/sendpage")
def sendpage():
    return {"reply": "Analysis Complete!"}
