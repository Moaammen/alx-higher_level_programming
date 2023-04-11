#!/usr/bin/python3

"""initial child class"""

class MyList(list):
    """class inhert from list"""

    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
