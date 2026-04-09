from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
import config

def load_documents():
    # Ensure folder exists
    if not os.path.exists(config.DATA_PATH):
        print(f"Creating data directory: {config.DATA_PATH}")
        os.makedirs(config.DATA_PATH, exist_ok=True)

    print(f"Current working directory: {os.getcwd()}")
    print(f"Data directory: {config.DATA_PATH}")

    files = os.listdir(config.DATA_PATH)
    pdf_files = [f for f in files if f.endswith('.pdf')]
    print(f"Files found in data directory: {files}")
    print(f"PDF files detected: {pdf_files}")

    if not pdf_files:
        print("[WARNING] No PDF files found in data folder. Skipping loading.")
        return []

    try:
        loader = DirectoryLoader(config.DATA_PATH, glob="*.pdf", loader_cls=PyPDFLoader)
        documents = loader.load()
        print(f"Successfully loaded {len(documents)} document sections.")
    except Exception as e:
        print(f"[ERROR] Error loading documents with PyPDFLoader: {e}")
        return []

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=config.CHUNK_SIZE,
        chunk_overlap=config.CHUNK_OVERLAP
    )

    splits = splitter.split_documents(documents)
    print(f"Split documents into {len(splits)} chunks.")
    return splits