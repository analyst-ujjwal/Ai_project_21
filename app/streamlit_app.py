import streamlit as st
from uuid import uuid4
from dotenv import load_dotenv
from memory_db import init_db
from agent import SupportAgent


load_dotenv()
init_db()


st.set_page_config(page_title="AI Customer Support Bot", page_icon="🤖", layout="wide")


st.title("Project-21 🤖 AI Customer Support Bot — Streamlit Edition")


if 'session_id' not in st.session_state:
    st.session_state.session_id = str(uuid4())


if 'messages' not in st.session_state:
    st.session_state.messages = []


agent = SupportAgent()


st.sidebar.markdown(f"**Backend:** {agent.backend}")


user_input = st.chat_input("Ask a question...")


if user_input:
    with st.spinner("Generating response..."):
        reply = agent.chat(st.session_state.session_id, user_input)
        st.session_state.messages.append(("You", user_input))
        st.session_state.messages.append(("AI", reply))


for sender, msg in st.session_state.messages:
    if sender == "You":
        st.markdown(f"**🧑‍💼 {sender}:** {msg}")
    else:
        st.markdown(f"**🤖 {sender}:** {msg}")