import os
from langchain_groq import ChatGroq

def get_groq_model(**kwargs):
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY not set in .env")
    # Default model — you can change it if needed
    model_name = kwargs.pop("model", "llama-3.1-8b-instant")
    return ChatGroq(api_key=api_key, model=model_name, **kwargs)
