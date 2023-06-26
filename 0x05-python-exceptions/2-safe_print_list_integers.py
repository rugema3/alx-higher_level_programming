#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for item in my_list[:x]:
            if isinstance(item, int):
                print("{:d}".format(item), end="")
                count += 1
    except IndexError:
        print("An exception occurred. The value of 'x' is larger than "
              "the length of 'my_list'.")
    else:
        print("\n")
    return count
