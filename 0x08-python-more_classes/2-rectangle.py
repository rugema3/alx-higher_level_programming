#!/usr/bin/python3
"""Defining class Rectangle."""


class Rectangle:
    """This is an empty class called Rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance.

        Args:
            width (int): The width of the  rectangle.
            height (int): The height of the rectangle.


        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the Rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Get the height of the Rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        """Set the height of the Rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """Calculate and return the area of a rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate and return the perimeter of a rectangle."""
        return 2 * (self.width + self.height)
