from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

# Absolute path to the data directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

def load_documents():
    # Ensure folder exists
    os.makedirs(DATA_DIR, exist_ok=True)

    print("Current working directory:", os.getcwd())
    print("Data directory:", DATA_DIR)

    files = os.listdir(DATA_DIR)
    print("Files in data:", files)

    if not files:
        print("⚠️ No PDF files found in data folder")
        return []

    loader = DirectoryLoader(DATA_DIR, glob="*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )

    return splitter.split_documents(documents)