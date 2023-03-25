#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b_dictionaty = {}
    for key in a_dictionary:
        b_dictionaty[key] = a_dictionary[key] * 2
    return b_dictionaty
