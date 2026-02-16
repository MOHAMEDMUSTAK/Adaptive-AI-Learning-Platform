import sqlite3

def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS performance (
            username TEXT,
            concept TEXT,
            correct INTEGER,
            response_time REAL
        )
    """)

    conn.commit()
    conn.close()

def save_performance(username, concept, correct, response_time):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("INSERT OR IGNORE INTO users (username) VALUES (?)", (username,))
    c.execute(
        "INSERT INTO performance VALUES (?, ?, ?, ?)",
        (username, concept, correct, response_time)
    )

    conn.commit()
    conn.close()

def get_user_data(username):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("SELECT concept, correct, response_time FROM performance WHERE username=?", (username,))
    data = c.fetchall()

    conn.close()
    return data
