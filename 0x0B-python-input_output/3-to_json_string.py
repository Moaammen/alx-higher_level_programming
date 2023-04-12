#!/usr/bin/python3

"""single function"""


import json


def to_json_string(my_obj):
    """function that returns the JSON representation of an object (string)"""
    json_str = json.dumps(my_obj)
    return json_str
