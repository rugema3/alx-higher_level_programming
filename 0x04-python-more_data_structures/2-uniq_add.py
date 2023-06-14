#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set(my_list)
    my_list = list(my_set)
    return sum(my_list)


"""
The above code implements the unique addition of elements in a list.
I have achieved it by first converting the list into a set.
This ensures that only unique elements are listed because in a set,
every element must be unique. After having a set, I converted the set
back to a list, but this time, my list had only unique elements.
And then I added the unique elements in a list.
"""
