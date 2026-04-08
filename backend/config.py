import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ==============================
# PROJECT PATHS
# ==============================

# Root project folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Data folder (PDFs)
DATA_PATH = os.path.join(BASE_DIR, "data")

# Vector database folder
VECTOR_DB_PATH = os.path.join(BASE_DIR, "backend", "vector_db")

# ==============================
# MODEL CONFIGURATION
# ==============================

# Embedding model
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# Chunking parameters
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# Retrieval settings
TOP_K_RESULTS = 3

# ==============================
# LLM CONFIG
# ==============================

# If using Groq
GROQ_API_KEY = os.getenv("GROQ_API_KEY")


# Model settings
LLM_TEMPERATURE = 0

# ==============================
# API CONFIG
# ==============================

API_HOST = "0.0.0.0"
API_PORT = 8000

# ==============================
# DEBUG
# ==============================

DEBUG = True
