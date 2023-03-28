#!/usr/bin/python3
"""create a class"""


class Square:
    """define size as private attr"""
    def __init__(self, size=0):
        """check if the size is not integer"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
            """check if the size is less than 0"""
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    """area method that return area by size power of 2"""
    def area(self):
        return self.__size ** 2
