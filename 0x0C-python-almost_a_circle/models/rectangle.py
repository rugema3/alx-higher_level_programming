#!/usr/bin/python3
"""This module defines the Rectangle class."""

from models.base import Base


class Rectangle(Base):
    """
    Define Rectangle class.

    Private instance attributes, each with its own public getter and setter:
    - __width -> width
    - __height -> height
    - __x -> x
    - __y -> y

    Class constructor:
    def __init__(self, width, height, x=0, y=0, id=None):
        Call the super class with id - this super call with use the
        logic of the __init__ of the Base class
        Assign each argument width, height, x, and y to the right attribute
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the Rectangle instance."""
        super().__init__(id)  # Call the _init_ method of Base class with id
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Define getter for the private attribute width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Define getter for private attribute width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("Width must be greater than zero")
        else:
            self.__width = value

    @property
    def height(self):
        """Define the getter for private attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Define the setter for private attribute height."""
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        elif value <= 0:
            raise ValueError("Height must be greater than zero")
        else:
            self.__height = value

    @property
    def x(self):
        """Define getter for private attribute x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Define setter for private attribute x."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Define getter for private attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Define the setter for private attribute."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Define area method."""
        return self.__width * self.__height