#!/usr/bin/python3
"""
A script to list all cities from a MySQL database using execute() once.

Usage:
    python script.py <username> <password> <database>

Arguments:
    <username>: MySQL username for database access.
    <password>: MySQL password for database access.
    <database>: Name of the MySQL database to connect to.

The script connects to a MySQL server running on localhost at port 3306
and retrieves all cities from the 'cities' table, including
their corresponding state names.
The results are displayed in ascending order by 'cities.id'.
"""

import MySQLdb
import sys


def list_cities(username, password, database):
    try:
        # Connect to the MySQL database
        db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database
        )

        # Create a cursor object to interact with the database
        cursor = db.cursor()

        # Execute the SQL query to select cities with their corresponding
        # state names
        cursor.execute("""
            SELECT cities.id, cities.name, states.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            ORDER BY cities.id
        """)

        # Fetch all the results returned by the query
        results = cursor.fetchall()

        # Iterate through the results and print each row
        for row in results:
            print(row)

    except MySQLdb.Error as err:
        # Handle any MySQL database errors and print an error message
        print("MySQL Error:", err)

    finally:
        # Ensure that the database connection is closed, whether or not an
        # error occurred
        if 'db' in locals():
            db.close()


if __name__ == "__main__":
    # Check for the correct number of command-line arguments (3)
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Extract the command-line arguments
    username, password, database = sys.argv[1:4]

    # Call the list_cities function with the provided arguments
    list_cities(username, password, database)
