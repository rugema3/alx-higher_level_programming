#!/usr/bin/python3
"""
A script that prints all City objects from the database hbtn_0e_14_usa.

Usage:
    python 14-model_city_fetch_by_state.py <username> <password> <database>

Arguments:
    <username>: MySQL username for database access.
    <password>: MySQL password for database access.
    <database>: Name of the MySQL database to connect to.

The script connects to a MySQL server running on localhost at port 3306,
fetches and prints all City objects, sorted by cities.id.
Results are displayed as follows: <state name>: (<city id>) <city name>.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def fetch_and_display_cities(username, password, database):
    """
    Fetch and print all City objects from the database.

    Args:
        username (str): MySQL username for database access.
        password (str): MySQL password for database access.
        database (str): Name of the MySQL database to connect to.
    """
    try:
        # Create a database engine and establish a connection
        engine = create_engine(
                f'mysql://{username}:{password}@localhost:3306/{database}')

        # Create a session to interact with the database
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query and fetch all City objects, sorted by cities.id
        cities = session.query(City).order_by(City.id).all()

        # Print the City objects in the specified format
        for city in cities:
            state_name = session.query(State.name).filter(
                    State.id == city.state_id).first()[0]
            print(f"{state_name}: ({city.id}) {city.name}")

    except Exception as e:
        # Handle any errors and print an error message
        print(f"Error: {e}")

    finally:
        # Close the session and the database connection
        if 'session' in locals():
            session.close()


if __name__ == "__main__":
    # Check for the correct number of command-line arguments (3)
    import sys

    if len(sys.argv) != 4:
        print(
            "Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Extract the command-line arguments
    username, password, database = sys.argv[1:4]

    # Call the fetch_and_display_cities function with the provided arguments
    fetch_and_display_cities(username, password, database)
