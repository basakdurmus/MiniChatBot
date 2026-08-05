import sys
import os

sys.path.append(r"C:\Users\ASUS\Desktop\MiniChatBot\backend")
from chatbot import ChatBot

bot = ChatBot()
response = bot.cevap_ver("Merhaba")
# Use encode to avoid terminal print errors with emojis
sys.stdout.buffer.write(response.encode("utf-8"))
