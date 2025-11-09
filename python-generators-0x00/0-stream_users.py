#!/usr/bin/python3

import mysql.connector
from seed import connect_to_prodev

def stream_users():
    connection = connect_to_prodev()
    if connection is None:
        return
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT user_id, name, email, age FROM user_data")

    for row in cursor:
        yield row

    cursor.close()
    connection.close()