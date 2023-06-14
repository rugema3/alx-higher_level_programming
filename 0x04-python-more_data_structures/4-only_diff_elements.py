#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    return set_1 ^ set_2


"""
This function returns a set of all elements present in only one set.
Please note that I could have used set_1 ^ set_2 to obtain similar
output. I just chose symmetric_difference() method to try something
new.
"""
