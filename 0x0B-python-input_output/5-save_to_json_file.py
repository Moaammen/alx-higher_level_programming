#!/usr/bin/python3
"""single function"""
import json


def save_to_json_file(my_obj, filename):
    """ function that writes an Object to a text file
    , using a JSON representation"""
    with open(filename, mode="w", encoding="utf-8") as f:
        new_obj = json.dumps(my_obj)
        f.write(new_obj)
