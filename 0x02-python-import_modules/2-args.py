#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 0
    arguments = sys.argv[i:]
    num = len(sys.argv) - 1
    print("{} {}:".format(num, 'argument' if num == 1 else 'arguments'))
    while num > 0:
        if num == 1:
            print("{}: {}".format(i+1, arguments[i+1]))
            break
        else:
            print("{}: {} ".format(i, arguments[i]))
            i += 1
            if i > num:
                break
