#!/usr/bin/python3
"""100-append_after module."""

def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """
    if not filename or not search_string or not new_string:
        return

    lines_list = []
    with open(filename, 'r') as file:
        lines_list = file.readlines()

    updated_lines = [line + new_string + '\n' if search_string in line
                     else line for line in lines_list]

    with open(filename, 'w') as file:
        file.writelines(updated_lines)
