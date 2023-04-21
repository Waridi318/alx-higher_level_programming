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
        self.__width = size
        self.__height = size

    def __str__(self):
        """String representation of square
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, super().x, super().y, self.__width
            )
