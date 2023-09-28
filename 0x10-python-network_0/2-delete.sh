#!/bin/bash
# a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response

# check if the URL argument is provided
if [ $# -ne 1 ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

url="$1"
curl -sX DELETE "$url"
