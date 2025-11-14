#!/usr/bin/python3
import sqlite3

with sqlite3.connect("users.db") as conn:
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT,
            age INTEGER
        )
    """)
    cur.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", ("Alice", "alice@example.com", 30))
    cur.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", ("Bob", "bob@example.com", 20))
    conn.commit()

print("DB created with age column.")

class ExecuteQuery:
    def __init__(self, query, params=()):
        """
        Initialize with a query string and optional parameters.
        """
        self.query = query
        self.params = params
        self.conn = None
        self.cursor = None
        self.result = None

    def __enter__(self):
        """
        Open the database, execute the query, and store the result.
        """
        self.conn = sqlite3.connect("users.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.query, self.params)
        self.result = self.cursor.fetchall()
        return self.result

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Commit changes and close the connection.
        """
        if self.conn:
            self.conn.commit()
            self.conn.close()


# Using the context manager
query_string = "SELECT * FROM users WHERE age > ?"
with ExecuteQuery(query_string, (25,)) as result:
    print(result)
