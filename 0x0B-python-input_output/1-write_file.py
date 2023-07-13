#!/usr/bin/python3
"""1-write_file module."""


def write_file(filename="", text=""):
    """Write contents to the file.

    Args:
    filename(str): The name of the file.
    text(str): the content to be written in a file.
    Return: the number of characters writen in the file.
    """
    with open(filename, 'w', encoding='utf-8') as filename:
        return filename.write(text)
