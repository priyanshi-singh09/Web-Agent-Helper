import os
import redis
import numpy as np
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
VECTOR_INDEX_PATH = "vector.index"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
SIM_THRESHOLD = 0.75

# Setup Redis
redis_client = redis.Redis.from_url(REDIS_URL)
