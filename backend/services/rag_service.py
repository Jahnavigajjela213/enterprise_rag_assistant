from document_loader import load_documents
from vector_store import get_vector_store
from core.llm import get_llm
from core.prompt import get_prompt
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

qa_engine = None
retriever = None


async def get_rag_engine():
    global qa_engine, retriever

    if qa_engine is None:
        print("[DEBUG] Initializing RAG engine...")
        try:
            print("[DEBUG] Loading documents...")
            splits = load_documents()
            
            if not splits:
                print("[ERROR] No PDF documents found.")
                raise Exception("No PDF documents found in the 'data' directory. Please add some PDF files and restart.")
            
            print(f"[DEBUG] Creating vector store with {len(splits)} splits...")
            vectorstore = get_vector_store(splits)

            retriever = vectorstore.as_retriever()

            print("[DEBUG] Initializing LLM...")
            llm = get_llm()
            
            print("[DEBUG] Loading prompt template...")
            prompt = get_prompt()

            def format_docs(docs):
                return "\n\n".join(doc.page_content for doc in docs)

            print("[DEBUG] Building QA chain...")
            qa_engine = (
                {"context": retriever | format_docs, "question": RunnablePassthrough()}
                | prompt
                | llm
                | StrOutputParser()
            )
            print("[SUCCESS] RAG engine initialized successfully.")

        except Exception as e:
            print(f"[ERROR] Failed to initialize RAG engine: {str(e)}")
            import traceback
            traceback.print_exc()
            raise e

    return qa_engine, retriever

