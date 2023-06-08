#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = sys.argv[1:]  # Exclude the script name from arguments
    num = len(arguments)  # Use len(arguments) instead of len(sys.argv) - 1
    print("{} {}:".format(num, 'argument' if num == 1 else 'arguments'))
    i = 0
    while num > 0:
        print("{}: {}".format(i + 1, arguments[i]))
        i += 1
        num -= 1
