from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.rag_service import get_rag_engine
import traceback

router = APIRouter()

# ==============================
# Request model
# ==============================
class QueryRequest(BaseModel):
    question: str


# ==============================
# Health Check Route
# ==============================
@router.get("/health")
def health():
    return {"status": "healthy"}


# ==============================
# Ask RAG Assistant
# ==============================
@router.post("/ask")
async def ask_question(request: QueryRequest):
    try:
        qa_engine, retriever = await get_rag_engine()

        if not qa_engine:
            raise HTTPException(
                status_code=500,
                detail="RAG engine not initialized."
            )

        # [SUCCESS] Pass string instead of dictionary
        answer = qa_engine.invoke(request.question)

        # [INFO] Retrieve source documents
        docs = retriever.invoke(request.question)

        sources = [
            {
                "file": doc.metadata.get("source", "").split("/")[-1],
                "page": doc.metadata.get("page", 0) + 1
            }
            for doc in docs
        ]

        return {
            "answer": answer,
            "sources": sources
        }

    except Exception as e:
        print("[ERROR] in /ask route:")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

