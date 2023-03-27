#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 1
    while True:
        try:
            print(*my_list[:x])
            i + = 1
            return i
        except IndexError:
            return
