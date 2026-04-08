# Enterprise RAG Assistant 🏢

The **Enterprise RAG Assistant** is an intelligent, high-performance Retrieval-Augmented Generation (RAG) system built to help employees and stakeholders seamlessly query human resources documentation, standard operating procedures (SOPs), and compliance manuals. 

By leveraging advanced natural language processing and vector search, the assistant provides rapid, contextually accurate answers based directly on the company's internal knowledge base, minimizing search time and improving organizational efficiency.

## 🌟 Key Features

* **Instant Document Question & Answering:** Ask natural language questions and get immediate answers grounded in your enterprise's internal documents.
* **Intelligent Source Attribution:** Every answer includes direct citations (source files and specific page references), ensuring complete transparency and trust in the generated information.
* **Modern & Responsive UI:** Built with Streamlit, the frontend features a sleek, fully responsive dark-mode interface designed for professionalism and ease of use.
* **Automated Document Extraction:** An automated pipeline for continuously loading, chunking, and embedding PDF documents into the vector database.
* **Extremely Fast Retrieval:** Employs a robust combination of FAISS (Facebook AI Similarity Search) and Sentence Transformers for sub-second semantic search results.

## 🏗 System Architecture

The project is structured into two completely decoupled components for maintainability and scale:

### 1. The Core AI Engine (Backend)
Built using **FastAPI** and **LangChain**, the resilient microservice handles the heavy lifting of the RAG pipeline.
* **Embedding Layer**: Processes chunks of documents and semantic queries using local HuggingFace `sentence-transformers`.
* **Vector Store**: Uses `faiss-cpu` to persistently index document embeddings for hyper-fast localized nearest-neighbor similarity searches.
* **Generation**: Integrates with robust large language models (facilitated by Groq) to synthesize final, human-readable answers from the retrieved semantic contexts. 

### 2. The User Interface (Frontend)
Built using **Streamlit**, serving as the client-facing access point. 
* Implements the user-facing chat paradigm.
* Maintains session states for an ongoing conversation experience.
* Connects asynchronously to the FastAPI backend over HTTP to process queries without locking up the UI.

## 📂 Project Structure

```text
enterprise-rag-assistant/
├── backend/
│   ├── api/             # API routing (FastAPI router definitions)
│   ├── core/            # Configs, Environment setups
│   ├── data/            # Source documents (PDFs, text)
│   ├── database/        # Local FAISS vector datastores
│   ├── services/        # Logic integrating LangChain + LLMs  
│   └── main.py          # FastAPI application entrypoint
├── frontend/
│   └── app.py           # The Streamlit dark-mode web application
└── start.sh             # Master script to synchronously boot both components
```

## 💻 Usage Commands

To run the application locally on your machine, you can use the following commands.

### 1. Unified Startup (Recommended)
This command will start both the backend FastAPI server and the frontend Streamlit application simultaneously.
```bash
# If using Linux/macOS
./start.sh

# If using Windows, you can explicitly run it with bash
bash start.sh
```

### 2. Manual Startup (Separate Terminals)
If you prefer to run and monitor them in separate terminal instances:

**Start the Backend:**
```bash
cd backend
uvicorn main:app --host 0.0.0.0 --port 8000
```

**Start the Frontend:**
```bash
cd frontend
streamlit run app.py
```

