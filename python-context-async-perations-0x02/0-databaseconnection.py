#!/usr/bin/python3

import sqlite3

with sqlite3.connect("users.db") as conn:
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT
        )
    """)
    conn.commit()

with sqlite3.connect("users.db") as conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Alice", "alice@example.com"))
    cur.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Bob", "bob@example.com"))
    conn.commit()


class DatabaseConnection:
    def __enter__(self):
        self.conn = sqlite3.connect("users.db")
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.commit()
        self.conn.close()


with DatabaseConnection() as query:
    query.execute("SELECT * FROM users")
    print(query.fetchall())
