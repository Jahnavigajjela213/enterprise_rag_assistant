from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

# Absolute path to the data directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

def load_documents():
    # Ensure folder exists
    if not os.path.exists(DATA_DIR):
        print(f"Creating data directory: {DATA_DIR}")
        os.makedirs(DATA_DIR, exist_ok=True)

    print(f"Current working directory: {os.getcwd()}")
    print(f"Data directory: {DATA_DIR}")

    files = os.listdir(DATA_DIR)
    pdf_files = [f for f in files if f.endswith('.pdf')]
    print(f"Files found in data directory: {files}")
    print(f"PDF files detected: {pdf_files}")

    if not pdf_files:
        print("⚠️ No PDF files found in data folder. Skipping loading.")
        return []

    try:
        loader = DirectoryLoader(DATA_DIR, glob="*.pdf", loader_cls=PyPDFLoader)
        documents = loader.load()
        print(f"Successfully loaded {len(documents)} document sections.")
    except Exception as e:
        print(f"❌ Error loading documents with PyPDFLoader: {e}")
        return []

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )

    splits = splitter.split_documents(documents)
    print(f"Split documents into {len(splits)} chunks.")
    return splits