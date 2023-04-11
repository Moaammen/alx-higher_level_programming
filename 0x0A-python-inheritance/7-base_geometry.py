#!/usr/bin/python3

"""initial class"""


class BaseGeometry:
    """Geometry class"""

    """Public instance method"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """check the value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
