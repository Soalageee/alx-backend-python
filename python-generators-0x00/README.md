# ALX Backend Project
## Overview

This project demonstrates how to set up a MySQL database using Python, populate it with data from a CSV file, and prepare it for further processing with Python generators. It is part of the ALX Backend Python learning program.

## Project Structure

```
python-generators-0x00/
├── 0-main.py        # Script to test seed.py functionality
├── seed.py          # Script to create database, table, and insert data
├── user_data.csv    # Sample user data to populate the database
└── README.md        # Project documentation 
```

## Objective

The main goal of this project is to:

- Create a MySQL database called ```ALX_prodev```.

- Create a table named ```user_data``` with the following fields:

```
user_id (Primary Key, UUID, Indexed)

name (VARCHAR, NOT NULL)

email (VARCHAR, NOT NULL)

age (DECIMAL, NOT NULL)
```

- Populate the table with sample data from ```user_data.csv```.

- Set up Python functions that can later be extended to stream rows one by one using generators.

## How It Works

### Connecting to MySQL Server:
Using the ```connect_db()``` function, Python connects to the MySQL server.

### Creating the Database:
The ```create_database()``` function ensures that the ```ALX_prodev``` database exists.

### Connecting to the Database:
The ```connect_to_prodev()``` function opens a connection directly to the ```ALX_prodev``` database.

### Creating the Table:
The ```create_table()``` function creates the ```user_data``` table with the required fields if it doesn’t already exist.

### Inserting Data:
The ```insert_data()``` function reads ```user_data.csv```, generates a unique UUID for each user, and inserts the data into the table while avoiding duplicates.

### Testing the Setup:
The ```0-main.py``` script checks that everything works correctly by:

- Creating the database and table

- Inserting sample data

- Fetching and printing the first 5 rows

Sample Data ```user_data.csv```
name	email	age
Dan Altenwerth Jr.	Molly59@gmail.com
	67
Glenda Wisozk	Miriam21@gmail.com
	119
Daniel Fahey IV	Delia.Lesch11@hotmail.com
	49
Ronnie Bechtelar	Sandra19@yahoo.com
	22
Alma Bechtelar	Shelly_Balistreri22@hotmail.com
	102

Note: ```user_id``` is generated automatically as a UUID for each user.