#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)  # Get the length of the sentence

    if length == 0:
        first = None  # Set first character to None if the sentence empty
    else:
        first = sentence[0]  # Get the first character of the sentence

    return length, first  # Return a tuple with length and first char
