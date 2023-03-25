#!/usr/bin/python3
def uniq_add(my_list=[]):
    result_ = 0
    my_set = set(my_list)
    for i in my_set:
        result_ += i
    return result_
