#!/usr/bin/python3
"""
This module defines a class rectangle
"""


class Rectangle:
    """
    This is a class rectangle
    """
    pass

    def __init__(self, width=0, height=0):
        """
        constructor of class instance
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        getter for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the attribute width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        retrieves height value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the value of height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
