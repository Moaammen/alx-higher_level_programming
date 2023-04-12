#!/usr/bin/python3

"""single function"""
import jason

def to_json_string(my_obj):
    """function that returns the JSON representation of an object (string)"""
    json_str = jason.dumps(my_obj)
    return json_str
