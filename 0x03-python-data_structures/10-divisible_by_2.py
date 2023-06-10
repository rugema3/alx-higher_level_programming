#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    for i in range(len(my_list)):
        for item in my_list:
            if item % 2 == 0:
                my_list[i] = True
            else:
                my_list[i] = False
