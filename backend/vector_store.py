from langchain_community.vectorstores import FAISS
from core.embeddings import get_embeddings
import os
import config

def get_vector_store(splits):
    try:
        embeddings = get_embeddings()
    except Exception as e:
        print(f"[ERROR] Failed to initialize embeddings: {e}")
        raise e

    # Try to load existing index
    if os.path.exists(config.VECTOR_DB_PATH) and os.path.exists(os.path.join(config.VECTOR_DB_PATH, "index.faiss")):
        try:
            print(f"[DEBUG] Loading existing vector store from {config.VECTOR_DB_PATH}")
            return FAISS.load_local(
                config.VECTOR_DB_PATH,
                embeddings,
                allow_dangerous_deserialization=True
            )
        except (Exception, AssertionError) as e:
            print(f"[WARNING] Could not load existing vector store (mismatch or corrupt): {e}")
            print("[DEBUG] Forcing a fresh index rebuild...")
            # If it's a dimensionality mismatch, we should delete the folder if it exists
            if os.path.exists(config.VECTOR_DB_PATH):
                import shutil
                try:
                    shutil.rmtree(config.VECTOR_DB_PATH)
                    print(f"[DEBUG] Deleted stale vector store at {config.VECTOR_DB_PATH}")
                except Exception as ex:
                    print(f"[ERROR] Could not delete stale vector store: {ex}")


    # Create new index if loading failed or index doesn't exist
    try:
        print(f"[DEBUG] Creating new FAISS index from {len(splits)} chunks...")
        vectorstore = FAISS.from_documents(splits, embeddings)
        
        # Ensure directory exists before saving
        os.makedirs(config.VECTOR_DB_PATH, exist_ok=True)
        vectorstore.save_local(config.VECTOR_DB_PATH)
        print(f"[SUCCESS] Vector store saved to {config.VECTOR_DB_PATH}")
        return vectorstore
    except Exception as e:
        print(f"[ERROR] Failed to create or save vector store: {e}")
        raise e

