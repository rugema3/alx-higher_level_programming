#!/usr/bin/python3
def search_replace(my_list, search, replace):
    indices = []
    new_list = my_list.copy()
    for idx, value in enumerate(new_list):
        if value == search:
            indices.append(idx)
            new_list[idx] = replace
    return new_list


"""
This program searches through a list and finds
the occerence of an element, only to replace it with a new element.
the used aproach is creating a new copy of the list while keeping
the original list intact.
The element is inserted in all indices where the element appears.
"""
