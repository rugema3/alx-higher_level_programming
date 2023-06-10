#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == None:
        return None # return none if the list is empty.
    else:
        sorted_list = sorted(my_list)
        return sorted_list[-1]
    """
    The sorted function will sort the list from the smallest number
    to the largest number.
    The last element on the list will have index -1 and this
    will be the maximum (larget number of the list.
    Please note that we could have used the max(my_list) to
    get the same output but this function was prohibited.
    """
