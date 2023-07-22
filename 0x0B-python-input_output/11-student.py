#!/usr/bin/python3
"""Define a student class."""


class Student():
    """Represent the class Student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance.

        Args:
            first_name (str): First name of the student.
            last_name (str): Last name of the student.
            age (int): Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.

        Args:
            attrs (list): Optional list of attribute names to retrieve.

        Returns:
            dict: Dictionary representation of the Student instance.
        """
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__

        json_dict = {}
        for attr in attrs:
            if isinstance(attr, str) and attr in self.__dict__:
                json_dict[attr] = self.__dict__[attr]
        return json_dict

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance.

        Args:
            json (dict): Dictionary containing attribute names and values.

        """
        if isinstance(json, dict):
            self.__dict__.clear()
            for key, value in json.items():
                setattr(self, key, value)
