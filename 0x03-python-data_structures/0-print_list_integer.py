#!/usr/bin/python3

def print_list_integer(my_list=[]):
    get_len = len(my_list)
    i = 0
    while i < get_len:
        print("{}".format(my_list[i]))
        i += 1
