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

    def my_print(self):
        """
        Public instance method that prints square in stdout
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()