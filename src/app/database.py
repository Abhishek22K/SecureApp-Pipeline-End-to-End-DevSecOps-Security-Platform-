import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATABASE = BASE_DIR / "database.db"
SCHEMA = BASE_DIR / "schema.sql"


def init_db():
    conn = sqlite3.connect(DATABASE)

    with open(SCHEMA, "r") as f:
        conn.executescript(f.read())

    conn.commit()
    conn.close()

    print("Database initialized successfully.")


if __name__ == "__main__":
    init_db()
