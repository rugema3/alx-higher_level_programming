#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """
    Replace an element in the list at the specified index position
    with a new value.
    If the index is out of range or negative, the original list is returned.

    Args:
        my_list (list): The original list.
        idx (int):The index position where the element sh'd be replaced.
        element: The new value to be inserted at the specified index.

    Returns:
        list: A modified list with the element replaced or the original
        list if the index is out of range.
    """

    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list

    """
    To replace an element at a specific position in a list without
    modifying the original list, we I have created a new list with
    the desired replacement:

    Created a copy of the original list to preserve its contents.
    Modified the copy by replacing the element at the desired position
    with the new value.
    Used the modified copy for further operations while keeping
    the original list intact.
    """
