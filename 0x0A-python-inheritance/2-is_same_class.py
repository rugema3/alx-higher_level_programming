#!/usr/bin/python3
"""2-is_same_class module."""


def is_same_class(obj, a_class):
    """Define is_same_class.

    Args:
    obj: an objec to be checked.
    a_class: a class to compare if an object belongs to.
    Return: True if an object belongs to class otherwise False.
    """
    if type(obj) == a_class:
        return True
    else:
        return False
