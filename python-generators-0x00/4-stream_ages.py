#!/usr/bin/python3

import mysql.connector
from seed import connect_to_prodev

def stream_users_ages():
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT age FROM user_data")

    for row in cursor:
        yield row["age"]

    connection.close()
    

def calculate_average_age():
    total_age = 0
    count = 0

    for age in stream_users_ages():
        total_age += age
        count += 1

    average = total_age / count if count > 0 else 0
    print(f"Average age of users: {average:.2f}") 


if __name__ == "__main__":
    calculate_average_age()
