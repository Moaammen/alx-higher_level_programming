#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = set(set_1).union(set_2)
    for i in set_1:
        for x in set_2:
            if i == x:
                new_set.remove(i)
    return new_set
