#!/usr/bin/python3
"""
This module define a square class
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

    @property
    def size(self):
        """
        retrieves private attribut size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        property setter to set private attribute size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Instance method that returns current square area
        """
        return self.__size * self.__size

    def __lt__(self, other):
        """
        Magic method that checks if area of self is less than
        area of other
        """
        return self.__size < other.__size

    def __le__(self, other):
        """
        Magic method that checks if area of self is less than
        or equal to area of other
        """
        return self.__size <= other.__size

    def __eq__(self, other):
        """
        Magic method that checks if area of self is equal
        to area of other
        """
        return self.__size == other.__size

    def __ne__(self, other):
        """
        Magic method that checks if area of self is
        not equal to area of other
        """
        return self.__size != other.__size

    def __gt__(self, other):
        """
        Magic method that checks if area of self is greater than
        area of other
        """
        return self.__size > other.__size

    def __e__(self, other):
        """
        Magic method that checks if area of self is greater than
        or equal to area of other
        """
        return self.__size >= other.__size
