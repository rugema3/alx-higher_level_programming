#!/usr/bin/python3
"""0-read_file module."""


def read_file(filename=""):
    """Read a text file."""
    with open(filename, 'r', encoding='utf-8') as filename:
        for line in filename:
            print(line, end="")
