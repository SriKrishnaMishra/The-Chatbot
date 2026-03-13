import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "llama-3.1-8b-instant"
)

VECTOR_DB_PATH = os.getenv(
    "VECTOR_DB_PATH",
    "vector_store"
)