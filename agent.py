import os
import redis
import numpy as np
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
VECTOR_INDEX_PATH = "vector.index"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
SIM_THRESHOLD = 0.75

# Setup Redis
redis_client = redis.Redis.from_url(REDIS_URL)

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("models/gemini-2.5-flash")
chat = model.start_chat()

def get_summary(text: str) -> str:
    try:
        response = chat.send_message(f"Summarize the following content: {text}")
        return response.text.strip()
    except Exception as e:
        print(f"Summarization error: {e}")
        return ""

