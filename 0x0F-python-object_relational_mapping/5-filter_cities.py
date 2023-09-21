#!/usr/bin/python3
"""
A script to list all cities of a given state from a MySQL database using
execute() once with prepared statements.

Usage:
    python script.py <username> <password> <database> <state_name>

Arguments:
    <username>: MySQL username for database access.
    <password>: MySQL password for database access.
    <database>: Name of the MySQL database to connect to.
    <state_name>: Name of the state for which you want to list cities.

The script connects to a MySQL server running on localhost at port 3306,
retrieves all cities of the specified state from the 'cities' table,
and displays the results in ascending order by 'cities.id'.
"""

import MySQLdb
import sys


def list_cities_by_state(username, password, database, state_name):
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

        # Execute the SQL query using prepared statements
        cursor.execute("""
            SELECT cities.id, cities.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id
        """, (state_name,))

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
    # Check for the correct number of command-line arguments (4)
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password>"
              "<database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Extract the command-line arguments
    username, password, database, state_name = sys.argv[1:5]

    # Call the list_cities_by_state function with the provided arguments
    list_cities_by_state(username, password, database, state_name)
