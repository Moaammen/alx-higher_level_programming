#!/usr/bin/python3

"""single function"""


def inherits_from(obj, a_class):
    """return true if its inherit from class"""

    return ((issubclass(type(obj), a_class)) and type(obj) != a_class)
