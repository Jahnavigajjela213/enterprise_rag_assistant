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
        splits = load_documents()
        
        if not splits:
            raise Exception("No PDF documents found in the 'data' directory. Please add some PDF files and restart.")
            
        vectorstore = get_vector_store(splits)

        retriever = vectorstore.as_retriever()

        llm = get_llm()
        prompt = get_prompt()

        def format_docs(docs):
            return "\n\n".join(doc.page_content for doc in docs)

        qa_engine = (
            {"context": retriever | format_docs, "question": RunnablePassthrough()}
            | prompt
            | llm
            | StrOutputParser()
        )

    return qa_engine, retriever
