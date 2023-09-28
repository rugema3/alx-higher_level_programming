#!/bin/bash
# a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
# Define the variables to be sent in the POST request
EMAIL="test@gmail.com"
SUBJECT="I will always be here for PLD"

# Use curl to send a POST request with the specified variables and display the response body
curl -s -X POST -d "email=$EMAIL&subject=$SUBJECT" "$1"
