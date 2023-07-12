#!/usr/bin/python3
"""1-my_list module."""


class MyList(list):
    """Define Mylist class."""

    def print_sorted(self):
        """Print the list in ascending order."""
        print(sorted(self))
