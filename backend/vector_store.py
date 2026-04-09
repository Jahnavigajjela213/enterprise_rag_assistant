from langchain_community.vectorstores import FAISS
from core.embeddings import get_embeddings
import os
import config

def get_vector_store(splits):
    embeddings = get_embeddings()

    if os.path.exists(os.path.join(config.VECTOR_DB_PATH, "index.faiss")):
        try:
            return FAISS.load_local(
                config.VECTOR_DB_PATH,
                embeddings,
                allow_dangerous_deserialization=True
            )
        except Exception as e:
            print(f"⚠️ Could not load existing vector store (perhaps model changed?): {e}")
            print("Regenerating index...")

    vectorstore = FAISS.from_documents(splits, embeddings)
    vectorstore.save_local(config.VECTOR_DB_PATH)
    return vectorstore
