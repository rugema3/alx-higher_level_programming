#!/usr/bin/python3
"""
A script to search for states in a MySQL database.

Usage:
    python script.py <username> <password> <database> <state_name>

Arguments:
    <username>: MySQL username for database access.
    <password>: MySQL password for database access.
    <database>: Name of the MySQL database to connect to.
    <state_name>: Name of the state to search for in the 'states' table.

The script connects to a MySQL server running on localhost at port 3306
and retrieves all rows from the 'states' table where the 'name' column
matches the provided <state_name>. The results are displayed in ascending
order by 'id'.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Check for the correct number of command-line arguments (4)
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password>"
              "<database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Extract the command-line arguments
    username, password, database, state_name = sys.argv[1:5]

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

        # Execute the SQL query to select states
        # where name matches the provided argument
        cursor.execute("""
            SELECT *
            FROM states
            WHERE name = %s
            ORDER BY id
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
