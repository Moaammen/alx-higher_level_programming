#!/usr/bin/python3
if __name__ == "__main__":
    """print arguments"""
from sys import argv
argv_len = len(argv)
i = 1
if argv_len > 1:

    print("{} arguments:".format(argv_len - 1))

    while i < argv_len:
        print("{}:".format(i), argv[i])
        i += 1
else:
    print("0 arguments.")
