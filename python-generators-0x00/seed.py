#!/usr/bin/python3

import mysql.connector
from mysql.connector import Error
import csv
import uuid

def connect_db():
    connection = None
    try: 
        connection = mysql.connector.connect(
            host = 'localhost',
            username = "root",
            password = "Admin35753_"
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None


def create_database(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        print("Database ALX_prodev created successfully")
    except Error as e:
        print(f"Error creating database: {e}")


def connect_to_prodev():
    connection = None
    try:
        connection = mysql.connector.connect(
            host = "localhost",
            username = "root",
            password = "Admin35753_",
            database = "ALX_prodev"
        )
        return connection
    except Error as e:
        print(f"Error connecting to ALX_prodev: {e}")
        return None


def create_table(connection):
    try: 
        cursor = connection.cursor()
        create_table_query = """
        CREATE TABLE IF NOT EXISTS user_data (
            user_id CHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL(3,0) NOT NULL
        )
        """
        cursor.execute(create_table_query)
        connection.commit()
        print("Table user_data created successfully")
    except Error as e:
        print(f"Error creating table: {e}")


def insert_data(connection, csv_file):
    try:
        cursor = connection.cursor()

        # Read data from CSV file
        with open(csv_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                user_id = str(uuid.uuid4())  # Generate a random UUID
                name = row['name']
                email = row['email']
                age = row['age']

                # Check if email already exists to avoid duplicates
                cursor.execute("SELECT * FROM user_data WHERE email = %s", (email,))
                existing = cursor.fetchone()
                if existing:
                    continue

                # Insert new record
                cursor.execute(
                    "INSERT INTO user_data (user_id, name, email, age) VALUES (%s, %s, %s, %s)",
                    (user_id, name, email, age)
                )

        connection.commit()
        print("Data inserted successfully from CSV")
    except Error as e:
        print(f"Error inserting data: {e}")