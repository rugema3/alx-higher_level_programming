#!/usr/bin/python3
"""0-lookup module."""


def lookup(obj):
    """Define lookup method.

    Args:
    obj: object to be parsed as an argument.

    Description:
    =============================================
    This function will return a list of available
    attributes and methods of an object.
    """
    if not isinstance(obj, object):
        raise ValueError("Invalid object. Object must"
                         "be an instance of a class.")

    try:
        return dir(obj)
    except Exception as e:
        print("Error occurred during attribute/method lookup:", str(e))
        return []
