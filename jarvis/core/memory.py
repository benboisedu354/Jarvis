import sqlite3
import os

DB_PATH = "data/memory.db"

def init_db():
    os.makedirs("data", exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS memory (
            role TEXT,
            text TEXT
        )
    """)

    conn.commit()
    conn.close()


def add(role, text):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO memory VALUES (?, ?)", (role, text))
    conn.commit()
    conn.close()


def get(limit=20):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT role, text FROM memory ORDER BY rowid DESC LIMIT ?", (limit,))
    rows = c.fetchall()
    conn.close()

    return list(reversed([
        {"role": r, "text": t} for r, t in rows
    ]))

def clear():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("DELETE FROM memory")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    clear()
    add("user", "Bonjour Jarvis")
    add("assistant", "Bonjour! Comment puis-je vous aider aujourd'hui?")
    print(get())
