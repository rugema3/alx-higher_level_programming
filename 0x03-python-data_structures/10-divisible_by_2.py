#!/usr/bin/python3
def divisible_by_2(my_list=None):
    if my_list is None:
        return None

    result = []
    for item in my_list:
        if item % 2 == 0:
            result.append(True)
        else:
            result.append(False)

    return result
