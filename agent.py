import os
import redis
import numpy as np
import google.generativeai as genai
from sentence_transformers import SentenceTransformer
import faiss
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

#Added get summary function
def get_summary(text: str) -> str:
    try:
        response = chat.send_message(f"Summarize the following content: {text}")
        return response.text.strip()
    except Exception as e:
        print(f"Summarization error: {e}")
        return ""

embedder = SentenceTransformer(EMBEDDING_MODEL)


if os.path.exists(VECTOR_INDEX_PATH):
    index = faiss.read_index(VECTOR_INDEX_PATH)
    with open(VECTOR_INDEX_PATH + '.keys', 'rb') as f:
        keys = np.load(f, allow_pickle=True).tolist()
else:
    dim = embedder.get_sentence_embedding_dimension()
    index = faiss.IndexFlatIP(dim)
    keys = 


def classify_query(query: str) -> bool:
    prompt = f"Is this a valid web search query? Answer YES or NO.\nQuery: {query}"
    try:
        response = chat.send_message(prompt)
        return response.text.strip().upper().startswith("YES")
    except Exception:
        return False


