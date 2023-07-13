#!/usr/bin/python3
"""Script to add arguments to a list and save to a JSON file."""


import sys
from typing import List
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


def add_arguments_to_list(arguments: List[str]):
    """
    Add arguments to a list and save to a JSON file.

    Args:
        arguments: A list of arguments to add to the existing data list.

    """
    try:
        # Load existing data from file
        existing_data = load_from_json_file("add_item.json")
    except FileNotFoundError:
        existing_data = []

    # Add new arguments to the list
    existing_data.extend(arguments)

    # Save the updated list to file
    save_to_json_file(existing_data, "add_item.json")


if __name__ == "__main__":
    # Skip the script name argument and pass the rest to add_arguments_to_list
    arguments = sys.argv[1:]
    add_arguments_to_list(arguments)
