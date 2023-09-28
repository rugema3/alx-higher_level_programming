#!/bin/bash
# A bash script that takes in a URL, sends a request to that URL, 
# and displays the size of the body of the response

# Get the URL from the command-line argument
URL="$1"

# Use curl to fetch the URL and pipe the output to wc to count bytes
curl -s "$URL" | wc -c
