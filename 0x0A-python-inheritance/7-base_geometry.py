#!/usr/bin/python3

"""initial class"""


class BaseGeometry:
    """Geometry class"""

    """Public instance method"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """check the value"""
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
