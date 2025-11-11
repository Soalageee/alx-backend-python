#!/usr/bin/python3

import sqlite3
import functools
from datetime import datetime

conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT
)
''')
# Optional: insert some test data
cursor.execute("INSERT INTO users (name, email) VALUES ('Soala', 'soala@example.com')")
conn.commit()
conn.close()


def log_queries(func):
    @functools.wraps(func)
    def wrapper_log_queries(*args, **kwargs):
        query = kwargs.get("query", args[0] if args else None)
        if query:
            print(f"{datetime.now()} - Executing SQL Query: {query}")
        else:
            print("No SQL query provided.")
        return func(*args, **kwargs)
    return wrapper_log_queries


@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")