#!/usr/bin/python3

import mysql.connector
from seed import connect_to_prodev

def stream_users_in_batches(batch_size):
    connection = connect_to_prodev()
    if connection is None:
        return

    cursor = connection.cursor(dictionary=True)

    offset = 0  # start from the first row
    while True:
        cursor.execute(
            "SELECT user_id, name, email, age FROM user_data LIMIT %s OFFSET %s",
            (batch_size, offset)
        )
        batch = cursor.fetchall()  # fetch all rows in this batch
        if not batch:
            break  # stop if no more rows

        yield batch  
        offset += batch_size
    cursor.close()
    connection.close()


def batch_processing(batch_size):
    for batch in stream_users_in_batches(batch_size):  
        for user in batch:  
            if user['age'] > 25:  
                print(user)  