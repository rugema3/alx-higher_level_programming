#!/bin/bash
# Displaying all the http methods available
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
