#!/usr/bin/python3
import sys
i = 0
arguments = sys.argv[i:]
num_args = len(sys.argv) - 1
print("{} {}:".format(num_args, 'argument' if num_args == 1 else 'arguments'))
while num_args > 0:
    if num_args == 1:
        print("{}: {}".format(i+1, arguments[i+1]))
        break
    else:
        print("{}: {} ".format(i, arguments[i]))

    i += 1
    if i > num_args:
        break
