#!/usr/bin/python3
"""101-add_attribute module."""


def add_attribute(obj, attribute, value):
    """
    Add a new attribute to an object if possible.

    Args:
        obj: The object to add the attribute to.
        attribute (str): The name of the attribute.
        value: The value of the attribute.

    Raises:
        TypeError: If the object can't have new attributes.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    obj.__setattr__(attribute, value)
