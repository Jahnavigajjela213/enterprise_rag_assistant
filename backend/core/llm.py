from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
import config

def get_llm():
    # 1. Primary Model: Gemini 2.5 Flash (via config)
    primary_llm = ChatOpenAI(
        model_name=config.PRIMARY_LLM_MODEL,
        temperature=config.LLM_TEMPERATURE,
        openai_api_key=config.OPENROUTER_API_KEY,
        openai_api_base=config.OPENROUTER_API_BASE
    )

    # 2. Fallback Model: Llama 3.3 (via config)
    fallback_llm = ChatGroq(
        model_name=config.FALLBACK_LLM_MODEL,
        temperature=config.LLM_TEMPERATURE,
        groq_api_key=config.GROQ_API_KEY
    )

    # 3. Combine with fallback logic
    llm_with_fallback = primary_llm.with_fallbacks([fallback_llm])
    
    return llm_with_fallback
