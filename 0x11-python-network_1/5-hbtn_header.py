#!/usr/bin/python3

"""
A script that:
- displays the X-Request-Id header variable of a request to a given URL
"""

import sys
import requests


def get_x_request_id(url):
    """
    Fetches the specified URL and returns the value of the
    X-Request-Id header.

    Args:
        url (str): The URL to fetch.

    Returns:
        str: The value of the X-Request-Id header, or
        None if the header is not found.
    """
    try:
        response = requests.get(url)
        x_request_id = response.headers.get("X-Request-Id")
        return x_request_id
    except requests.exceptions.RequestException as e:
        # Handle any request-related errors
        print("Error:", e)
        return None


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    x_request_id = get_x_request_id(url)

    if x_request_id:
        print("X-Request-Id:", x_request_id)
    else:
        print("X-Request-Id header not found in the response.")
