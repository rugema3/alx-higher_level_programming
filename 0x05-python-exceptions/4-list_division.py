#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    try:
        for i in range(list_length):
            try:
                dividend = my_list_1[i]
                divisor = my_list_2[i]
                if not isinstance(dividend, (int, float)) or \
                   not isinstance(divisor, (int, float)):
                    raise TypeError("wrong type")
                if divisor == 0:
                    raise ZeroDivisionError("division by 0")
                result.append(dividend / divisor)
            except ZeroDivisionError:
                print("division by 0")
                result.append(0)
            except TypeError:
                print("wrong type")
                result.append(0)
            except IndexError:
                print("out of range")
                result.append(0)
    finally:
        return result
