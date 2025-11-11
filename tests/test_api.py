from app.agent import SupportAgent
from uuid import uuid4


def test_chat():
    agent = SupportAgent()
    session = str(uuid4())
    reply = agent.chat(session, "Hello")
    assert isinstance(reply, str)
    assert len(reply) > 0