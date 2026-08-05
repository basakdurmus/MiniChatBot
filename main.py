from fastapi import FastAPI
from pydantic import BaseModel
from chatbot import ChatBot

app = FastAPI()

bot = ChatBot()


class Message(BaseModel):
    message: str


@app.get("/")
def home():
    return {
        "message": "BaşakGPT API çalışıyor 🚀"
    }


@app.post("/chat")
def chat(data: Message):

    cevap = bot.cevap_ver(data.message)

    return {
        "user": data.message,
        "bot": cevap
    }