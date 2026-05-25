import sqlite3
from pathlib import Path

DB_NAME = "tasks.db"

def initialize_database():
    db_exists = Path(DB_NAME).exists()

    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        priority INTEGER,
        is_done INTEGER DEFAULT 0
    )
    """)

    connection.commit()
    connection.close()

    if not db_exists:
        print("Database created.")
    else:
        print("Database already exists.")

