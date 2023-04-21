#!/usr/bin/python3

"""
This module defines a class that inherits from Rectangle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """This is a sub class of Rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor
        """
        super().__init__(size, size, x, y, id)
        self.__size = size

    @property
    def size(self):
        """
        getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter for width
        """
        if type(value) is not (int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be >= 0")
        else:
            self.__size = value
            self.__width = value
            self.__height = value

    def __str__(self):
        """String representation of square
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, super().x, super().y, self.__size
            )
