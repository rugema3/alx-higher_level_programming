#!/usr/bin/python3
"""3-is_kind_of_class module."""


def is_kind_of_class(obj, a_class):
    """Define the function.
    
    Description:
    This checks if an object belongs
    to a class or its subclasses.

    Args:
    obj: object to be compared.
    a_class: a class to be compared.
    Return: True if it belongs to a class or subclass, False otherwise.
    """
    if isinstance(object, a_class) or issubclass(type(obj), a_class):
        return True
    return False
