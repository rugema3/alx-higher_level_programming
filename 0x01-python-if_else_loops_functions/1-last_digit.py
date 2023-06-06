#!/usr/bin/python3
import random
n = random.randint(-10000, 10000)
rem = abs(n) % 10

if n >= 0:
    if rem > 5:
        print(f"Last digit of {n:d} is {rem:d} and is greater than 5")
    elif rem < 6 and rem != 0:
        print(f"Last digit of {n:d} is {rem:d} and is less than 6 and not 0")
    else:
        print(f"Last digit of {n:d} is {rem:d} and is 0")
else:
    if rem != 0:
        print(f"Last digit of {n:d} is -{rem:d} and is less than 6 and not 0")
    else:
        print(f"Last digit of {n:d} is {rem:d} and is 0")
