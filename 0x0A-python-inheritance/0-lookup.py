#!/usr/bin/python3

"""function look up"""


def lookup(obj):
    """returns the list of available attributes and methods of an object"""

    lis = []
    lis = dir(obj)
    return lis
