from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from chatbot import ChatBot

app = FastAPI()

# React'in API'ye erişebilmesi için
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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