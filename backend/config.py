import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ==============================
# PROJECT PATHS
# ==============================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Data folder (PDFs)
DATA_PATH = os.path.join(BASE_DIR, "data")

# Vector database folder
VECTOR_DB_PATH = os.path.join(BASE_DIR, "vector_db")

# ==============================
# MODEL CONFIGURATION
# ==============================

# Embedding model (OpenRouter)
EMBEDDING_MODEL = "openai/text-embedding-3-small"
OPENROUTER_API_BASE = "https://openrouter.ai/api/v1"

# LLM models
PRIMARY_LLM_MODEL = "google/gemini-2.5-flash"
FALLBACK_LLM_MODEL = "llama-3.3-70b-versatile"

# Chunking parameters
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# Retrieval settings
TOP_K_RESULTS = 3

# ==============================
# API KEYS
# ==============================

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# ==============================
# MODEL SETTINGS
# ==============================

LLM_TEMPERATURE = 0

# ==============================
# SERVER CONFIG
# ==============================

API_HOST = "0.0.0.0"
API_PORT = 8000
DEBUG = True
