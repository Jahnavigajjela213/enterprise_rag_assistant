import os
from dotenv import load_dotenv

# FORCE correct path
load_dotenv()

from langchain_groq import ChatGroq


def get_llm():
    return ChatGroq(
        model_name="llama-3.3-70b-versatile",
        temperature=0,
        groq_api_key=os.getenv("GROQ_API_KEY")
    )
