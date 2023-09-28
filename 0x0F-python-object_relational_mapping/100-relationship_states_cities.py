#!/usr/bin/python3
"""
A script that creates the State "California" with the City "San Francisco"
from the database hbtn_0e_100_usa.

Usage:
    python 100-relationship_states_cities.py <username> <password> <database>

Arguments:
    <username>: MySQL username for database access.
    <password>: MySQL password for database access.
    <database>: Name of the MySQL database to connect to.

The script connects to a MySQL server running on localhost at port 3306,
creates the State "California" and the City "San Francisco",
and associates them using the cities relationship for all State objects.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


def setup_state_and_city(username, password, database):
    """
    Create the State "California" with the City "San Francisco" .
    And associate them.

    Args:
        username (str): MySQL username for database access.
        password (str): MySQL password for database access.
        database (str): Name of the MySQL database to connect to.
    """
    try:
        # Create a database engine and establish a connection
        engine = create_engine(
                f'mysql://{username}:{password}@localhost:3306/{database}')

        # Create all tables defined in the Base
        Base.metadata.create_all(engine)

        # Create a session to interact with the database
        Session = sessionmaker(bind=engine)
        session = Session()

        # Create the State "California"
        california = State(name="California")

        # Create the City "San Francisco" and associate it with California
        san_francisco = City(name="San Francisco", state=california)

        # Add the City to California's cities relationship
        california.cities.append(san_francisco)

        # Add California to the session and commit the changes
        session.add(california)
        session.commit()

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

    # Call the setup_state_and_city function with the provided arguments
    setup_state_and_city(username, password, database)
