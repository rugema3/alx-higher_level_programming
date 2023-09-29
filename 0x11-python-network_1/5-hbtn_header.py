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

    """
    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))

if __name__ == '__main__':
    get_e_request_id(url)
