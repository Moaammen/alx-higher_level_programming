#!/usr/bin/python3
if __name__ == "__main__":
    """infinite_add"""
from sys import argv
argv_len = len(argv)
i_add = 0
i = 1
if argv_len > 1:

    while i < argv_len:
        i_add += int(argv[i])
        i += 1
    print("{}".format(i_add))
else:
    print("0")
