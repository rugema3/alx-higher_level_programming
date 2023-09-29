#!/usr/bin/python3

"""
A script that sends a POST request to a URL with an email parameter
and displays the body of the response (decoded in utf-8).
Usage:
    $ ./script.py <URL> <email>
"""

import sys
import urllib.request
import urllib.parse


def send_post_request(url, email):
    """
    Sends a POST request to the specified URL with the email as a parameter.

    Args:
        url (str): The URL to send the POST request to.
        email (str): The email to include as a parameter.

    Returns:
        None
    """
    try:
        # Encode the email parameter
        data = urllib.parse.urlencode({'email': email}).encode('utf-8')

        # Send the POST request and get the response
        with urllib.request.urlopen(url, data=data) as response:
            # Read and decode the response body
            body = response.read().decode('utf-8')

            print("Response body:")
            print(body)
    except urllib.error.URLError as e:
        # Handle any URL-related errors
        print("Error:", e)


if __name__ == "__main__":
    # Check if both URL and email arguments are provided
    if len(sys.argv) != 3:
        print("Usage: ./script.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]
    send_post_request(url, email)
