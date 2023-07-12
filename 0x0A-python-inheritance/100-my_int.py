#!/usr/bin/python3
"""100-my_int module."""


class MyInt(int):
    """A class representing a rebellious integer, inheriting from int."""

    def __eq__(self, other):
        """
        Override the == operator.

        Args:
            other: The object to compare with.

        Returns:
            bool: True if the values are not equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Override the != operator.

        Args:
            other: The object to compare with.

        Returns:
            bool: True if the values are equal, False otherwise.
        """
        return super().__eq__(other)
