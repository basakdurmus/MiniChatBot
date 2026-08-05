import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv(r"C:\Users\ASUS\Desktop\MiniChatBot\backend\.env")
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

models_to_test = [
    "gemini-2.5-flash-lite", 
    "gemini-2.0-flash-lite", 
    "gemini-pro-latest", 
    "gemini-flash-latest",
    "gemini-2.0-flash-lite-001"
]

for m in models_to_test:
    print(f"Testing {m}...")
    model = genai.GenerativeModel(m)
    try:
        res = model.generate_content("hello")
        print(f"SUCCESS: {m}")
        break
    except Exception as e:
        print(f"FAILED: {m} - {e}")
