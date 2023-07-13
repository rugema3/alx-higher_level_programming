#!/usr/bin/python3
"""Define a student class."""


class Student():
    """Represent the class Student."""

    def __init__(self, first_name, last_name, age):
        """Init method.

        Args:
        first_name(str): first name of the student.
        last_name(str): The last name of the student.
        age(int): the age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieve a dictionary representation of a Student instance."""
        return self.__dict__
