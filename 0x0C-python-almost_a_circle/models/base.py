#!/usr/bin/python3
"""Base module."""


class Base:
    """Define class named Base."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Init method of the base Class."""
        if self.id is not None:
            self.id = id
        else:
            __nb_objects = __nb_objects + 1
            self.id = __nb_objects
