#!/usr/bin/python3

if __name__ == "__main__":

    import hidden_4

    my_names = dir(hidden_4)
    for name in my_names:
        if name[:2] != "__":
            print(name)
