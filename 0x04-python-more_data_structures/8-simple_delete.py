#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    a_dictionary.pop(key, None)
    return a_dictionary


"""
This function deletes a key from the dictionary. Please note
that the key will be deleted together with its corresponding value.
we used the pop() method which returns the value of the popped key.
It return nothing if the value doesn't exisit.
"""
