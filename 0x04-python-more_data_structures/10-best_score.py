#!/usr/bin/python3
def best_score(a_dictionary):
    """return none if dict in empty"""
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    max_val = max(a_dictionary.values())
    for key in a_dictionary:
        if a_dictionary[key] == max_val:
            return key
