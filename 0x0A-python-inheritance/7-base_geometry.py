#!/usr/bin/python3
"""7-base_geometry module."""


class BaseGeometry:
    """Define an empty class."""

    def area(self):
        """Define method area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Define integer_validator.

        Args:
        name(str): The name
        value(int): The integer to be valiadated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
