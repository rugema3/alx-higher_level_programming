#!/usr/bin/python3
"""4-from_json_string module."""


import json


def from_json_string(my_str):
    """Define the method.
    Description:
    This function converts Json into a
    python object.

    Arggs:
    my_str: a json string to be converted into a python object.
    Return: a python object.
    """
    return json.loads(my_str)
