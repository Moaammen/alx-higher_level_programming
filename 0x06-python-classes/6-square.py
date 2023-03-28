#!/usr/bin/python3
"""create a class"""


class Square:
    """define size as private attr"""
    def __init__(self, size=0, position=(0, 0)):
        """check if the size is not integer"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple)
                or not all(isinstance(num, int)for num in value)
                or not all(num >= 0 for num in value) or len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for y in range(self.__position[1]):
                print("", end="")
            for i in range(self.__size):
                for s in range(self.__position[0]):
                    print(" ", end="")
                for x in range(self.__size):
                    print("#", end="")
                print("")
