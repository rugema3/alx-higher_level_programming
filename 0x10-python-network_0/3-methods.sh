#!/bin/bash
# Displaying all the http methods available
curl -sI -X OPTIONS "$1" | grep -iE '^Allow:' | awk '{print $2}'
