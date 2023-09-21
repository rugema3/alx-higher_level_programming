# relationship_state.py

#!/usr/bin/python3
"""
Module that contains the class definition of a State.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from model_city import Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData

custom_metadata = MetaData()
Base = declarative_base(metadata=custom_metadata)
class State(Base):
    """
    State class that represents a state and links to the MySQL table states.
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states")
