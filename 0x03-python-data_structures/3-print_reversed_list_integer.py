#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    get_len = len(my_list) - 1
    while get_len >= 0:
        print("{:d}".format(my_list[get_len]))
        get_len -= 1
