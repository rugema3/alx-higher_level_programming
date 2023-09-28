#!/bin/bash
# A bash script that takes in a URL, sends a request to that URL, 
# and displays the size of the body of the response

# Check if the URL argument is provided
if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Get the URL from the command-line argument
URL="$1"

# Use curl to fetch the URL and pipe the output to wc to count bytes
response_size=$(curl -s "$URL" | wc -c)

# Display the size of the response body in bytes
echo "$response_size"
