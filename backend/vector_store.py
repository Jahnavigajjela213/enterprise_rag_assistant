from langchain_community.vectorstores import FAISS
from core.embeddings import get_embeddings
import os

# Absolute path to the vector_db directory (next to this file)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VECTOR_DB_PATH = os.path.join(BASE_DIR, "vector_db")

def get_vector_store(splits):
    embeddings = get_embeddings()

    if os.path.exists(os.path.join(VECTOR_DB_PATH, "index.faiss")):
        try:
            return FAISS.load_local(
                VECTOR_DB_PATH,
                embeddings,
                allow_dangerous_deserialization=True
            )
        except Exception as e:
            print(f"⚠️ Could not load existing vector store (perhaps model changed?): {e}")
            print("Regenerating index...")

    vectorstore = FAISS.from_documents(splits, embeddings)
    vectorstore.save_local(VECTOR_DB_PATH)
    return vectorstore
