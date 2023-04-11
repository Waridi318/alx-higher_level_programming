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
        """
        try:
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        except TypeError as e:
            print(e)
        except ValueError as e:
            print(e)
