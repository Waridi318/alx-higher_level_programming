#!/usr/bin/python3
"""
This is a module that defines a class square
"""


class Square:
    """This defines a class square
    """
    def __init__(self, size=0):
        """
        Constructor for the square class

        Args:
            size(int): size of square

        Raises:
            TypeError: if size not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Instance method that returns current square area
        """
        return self.__size * self.__size
