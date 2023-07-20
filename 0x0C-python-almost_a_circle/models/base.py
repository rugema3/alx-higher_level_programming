#!/usr/bin/python3
"""Base module."""

import json


class Base:
    """Define class named Base."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Init method of the base Class."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON string."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save JSON string representation of list_objs to a file."""
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            obj_dicts = [obj.to_dictionary() for obj in list_objs]
            json_string = cls.to_json_string(obj_dicts)
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation json_string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)
