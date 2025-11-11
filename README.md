🤖 AI Customer Support Bot — Streamlit Edition

An intelligent customer support chatbot built with LangChain and Groq, running entirely in Streamlit. This lightweight prototype helps you simulate a conversational support assistant capable of remembering context and switching between Groq’s cloud models or a local LLaMA backend.

🚀 Features

🧠 LangChain-powered reasoning — easily switch between local and hosted LLMs.

⚡ Groq integration — blazing-fast inference with llama-3.1-8b-instant by default.

💬 Persistent chat memory — uses a simple SQLite DB to store conversation history.

🪶 Streamlit-only architecture — no backend server needed.

🔄 Auto model fallback — if Groq API is missing, switches to local LLaMA automatically.

🧰 Tech Stack

Streamlit — UI + app runner

LangChain — LLM orchestration

Groq — hosted model inference

SQLite — lightweight memory persistence

Python 3.10+