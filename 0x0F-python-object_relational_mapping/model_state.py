#!/usr/bin/python3
"""This module contains a class definition of a State.
And an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create an instance of declarative_base
Base = declarative_base()

# Define the State class


class State(Base):
    """Define State class.
    Attributes:
    id(int): The id of a state.
    name(string): The name of the state
    """
    __tablename__ = 'states'  # Name of the MySQL table

    # Columns
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
