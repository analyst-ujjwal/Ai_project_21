from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from groq_client import get_groq_model
from local_llama import get_local_llama
from memory_db import save_message, load_session
import os


class SupportAgent:
    def __init__(self):
        self.backend = 'groq' if os.getenv('GROQ_API_KEY') else 'local'
        self.model = get_groq_model() if self.backend == 'groq' else get_local_llama()


    def chat(self, session_id: str, user_input: str) -> str:
        history = load_session(session_id)
        messages = [SystemMessage(content="You are a polite and knowledgeable AI customer support assistant.")]
        for role, content in history:
            if role == 'user':
                messages.append(HumanMessage(content=content))
            else:
                messages.append(AIMessage(content=content))
        messages.append(HumanMessage(content=user_input))


        response = self.model.generate(messages=[messages]) if hasattr(self.model, 'generate') else self.model(messages)


        if hasattr(response, 'generations'):
            text = response.generations[0][0].text
        elif isinstance(response, str):
            text = response
        else:
            text = str(response)


        save_message(session_id, 'user', user_input)
        save_message(session_id, 'assistant', text)
        return text