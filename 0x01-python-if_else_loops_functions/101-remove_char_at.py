#!/usr/bin/python3
def remove_char_at(string, n):
    if n < 0 or n >= len(string):
        return string

    new_string = ""
    for index in range(len(string)):
        if index != n:
            new_string += string[index]

    return new_string
