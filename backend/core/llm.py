import os
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq

def get_llm():
    # 1. Primary Model: Gemini 2.5 Flash (via OpenRouter)
    primary_llm = ChatOpenAI(
        model_name="google/gemini-2.5-flash",
        temperature=0,
        openai_api_key=os.getenv("OPENROUTER_API_KEY"),
        openai_api_base="https://openrouter.ai/api/v1"
    )

    # 2. Fallback Model: Llama 3.3 (via Groq)
    fallback_llm = ChatGroq(
        model_name="llama-3.3-70b-versatile",
        temperature=0,
        groq_api_key=os.getenv("GROQ_API_KEY")
    )

    # 3. Combine with fallback logic
    # If the primary model fails (e.g. rate limit, outage), it switches to the fallback
    llm_with_fallback = primary_llm.with_fallbacks([fallback_llm])
    
    return llm_with_fallback
