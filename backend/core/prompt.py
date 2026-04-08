from langchain_core.prompts import ChatPromptTemplate


def get_prompt():
    return ChatPromptTemplate.from_template(
        """
You are an enterprise knowledge assistant.
Answer the question based on the context below.

Context:
{context}

Question:
{question}
"""
    )
