from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
import config

def load_documents():
    # Ensure folder exists
    if not os.path.exists(config.DATA_PATH):
        print(f"[DEBUG] Creating data directory: {config.DATA_PATH}")
        os.makedirs(config.DATA_PATH, exist_ok=True)

    print(f"[DEBUG] Current working directory: {os.getcwd()}")
    print(f"[DEBUG] Data directory being searched: {config.DATA_PATH}")

    try:
        files = os.listdir(config.DATA_PATH)
        pdf_files = [f for f in files if f.endswith('.pdf')]
        print(f"[DEBUG] Files found in data directory: {files}")
        print(f"[DEBUG] PDF files detected: {pdf_files}")

        if not pdf_files:
            print("[WARNING] No PDF files found in data folder. Skipping loading.")
            return []

        print(f"[DEBUG] Attempting to load {len(pdf_files)} PDFs from {config.DATA_PATH}...")
        loader = DirectoryLoader(config.DATA_PATH, glob="*.pdf", loader_cls=PyPDFLoader)
        documents = loader.load()
        print(f"[SUCCESS] Successfully loaded {len(documents)} document sections.")
        
    except Exception as e:
        print(f"[ERROR] Error during document loading phase: {str(e)}")
        import traceback
        traceback.print_exc()
        return []

    try:
        print(f"[DEBUG] Splitting {len(documents)} document sections into chunks...")
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=config.CHUNK_SIZE,
            chunk_overlap=config.CHUNK_OVERLAP
        )

        splits = splitter.split_documents(documents)
        print(f"[SUCCESS] Split documents into {len(splits)} chunks.")
        return splits
    except Exception as e:
        print(f"[ERROR] Error during text splitting phase: {str(e)}")
        import traceback
        traceback.print_exc()
        return []