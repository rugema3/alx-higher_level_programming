#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    return list(map(lambda x: x * number, my_list))


"""
This function multplies each element in a list
by a constant called "number".

It then returns a new list.
we are using map and lambda to achieve this in exactly 3 lines of code
"""
