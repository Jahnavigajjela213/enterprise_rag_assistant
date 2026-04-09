from langchain_openai import OpenAIEmbeddings
import config

def get_embeddings():
    # Use OpenRouter's OpenAI-compatible endpoint via config
    return OpenAIEmbeddings(
        model=config.EMBEDDING_MODEL,
        openai_api_key=config.OPENROUTER_API_KEY,
        openai_api_base=config.OPENROUTER_API_BASE
    )
