import sqlite3
from typing import List, Tuple


DB_PATH = "conversations.db"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
    """
    CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id TEXT,
    role TEXT,
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """
    )
    conn.commit()
    conn.close()




def save_message(session_id: str, role: str, content: str):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("INSERT INTO messages (session_id, role, content) VALUES (?, ?, ?)", (session_id, role, content))
    conn.commit()
    conn.close()




def load_session(session_id: str) -> List[Tuple[str, str]]:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT role, content FROM messages WHERE session_id = ? ORDER BY id", (session_id,))
    rows = cur.fetchall()
    conn.close()
    return rows