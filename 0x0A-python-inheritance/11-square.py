#!/usr/bin/python3
"""
This module defines a grandchild class of class BaseGeometry
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    subclass of class Rectangle
    """

    def __init__(self, size):
        """
        Construtor
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
        self.area()

    def __str__(self):
        """
        stirng representation of square
        """
        return ("[Square] {}/{}".format(self.__size, self.__size))
