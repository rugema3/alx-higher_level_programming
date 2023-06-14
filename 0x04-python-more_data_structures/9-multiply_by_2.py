#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()
    for key in new_dictionary:
        new_dictionary[key] *= 2
    return new_dictionary


"""
This function first copies the original dictionary so that
the changes made to the copy won't affect the original dictionary.

It then iterates through the keys of the dictionary and
multiplies the values by a constant.
This way, the original dictionary remains intact.
"""
