#!/usr/bin/python3
def divisible_by_2(my_list=None):
    if my_list is None:
        return None

    result = [None] * len(my_list)

    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            result[i] = True
        else:
            result[i] = False

    return result
