import sqlite3

DB_NAME = "tasks.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        text TEXT,
        remind_at TEXT
    )
    """)
    conn.commit()
    conn.close()

def add_task(user_id, text, remind_at):
    conn = sqlite3.connect(DB_NAME)
    conn.execute("INSERT INTO tasks (user_id, text, remind_at) VALUES (?, ?, ?)",
                 (user_id, text, remind_at))
    conn.commit()
    conn.close()
