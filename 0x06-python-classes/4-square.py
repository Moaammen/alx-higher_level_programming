#!/usr/bin/python3
"""create a class"""


class Square:
    """define size as private attr"""
    def __init__(self, size=0):
        """check if the size is not integer"""
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
            """check if the size is less than 0"""
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    """area method that return area by size power of 2"""

    def area(self):
        return self.__size ** 2
