#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    get_len = len(my_list)
    if idx < 0 or idx >= get_len:
        return my_list
    else:
        my_list[idx] = element
        return my_list
