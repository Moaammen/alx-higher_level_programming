#!/usr/bin/python3
"""subclass rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """inherit from BaseGeometry"""

    def __init__(self, width, height):

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height


def area(self):
    """calculate the area of rectangle"""
    return (self.__width * self.__height)


def __str__(self):
    """set the printed string"""
    string = "[Rectangle] {}/{}".format(self.__width, self.__height)
    return string
