#!/usr/bin/python3

"""create class that defines a rectangle"""


class Rectangle:
    """create class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
    """define width as private attr"""
    @property
    def width(self):
        """getter method"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter method"""
        if not isinstance(value):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method"""
        if not isinstance(value):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
