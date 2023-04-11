#!/usr/bin/python3
"""subclass Square inherit from rectangle class"""

Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """inherit from Rectangle"""

    def __init__(self, size):

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
