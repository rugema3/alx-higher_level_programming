#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    value_list = list(a_dictionary.values())
    if not value_list:
        return None
    else:
        max_score = max(value_list)
        for key in a_dictionary:
            if a_dictionary[key] == max_score:
                return key


"""
This function checks for the best score among the students.
It first converts the values of a dictionary into a list.
It then checks for the maximum score using the max() function.

It finally goes on to iterate through the dictionary to find the key
that corresponds with the value obtained. Once the key is found,
the function return the key which is this case is the name
of the student.
"""
