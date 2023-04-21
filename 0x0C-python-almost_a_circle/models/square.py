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
        getter for size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter for size
        """
        self.__size = value
        self.width = value
        self.height = value

    def __str__(self):
        """String representation of square
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, super().x, super().y, self.__size
            )
