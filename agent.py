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


def search_vector_cache(query: str):
    vec = embedder.encode(query.lower())
    faiss.normalize_L2(vec.reshape(1, -1))
    if index.ntotal == 0:
        return None
    D, I = index.search(vec.reshape(1, -1), 1)
    if D[0][0] >= SIM_THRESHOLD:
        orig_q = keys[I[0][0]]
        return redis_client.get(orig_q).decode()
    return None

def store_cache(query: str, result: str):
    redis_client.set(query, result)
    vec = embedder.encode(query.lower())
    faiss.normalize_L2(vec.reshape(1, -1))
    index.add(vec.reshape(1, -1))
    keys.append(query)
    faiss.write_index(index, VECTOR_INDEX_PATH)
    with open(VECTOR_INDEX_PATH + '.keys', 'wb') as f:
        np.save(f, np.array(keys, dtype=object))

