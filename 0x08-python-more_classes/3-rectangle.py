#!/usr/bin/python3
"""
This module defines a class rectangle
"""


class Rectangle:
    """
    This is a class rectangle
    """

    def __init__(self, width=0, height=0):
        """
        constructor of class instance
        """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
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

    def area(self):
        """
        public instance method that returns rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        public instance method that returns the
        perimeter of the rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """
        prints rectangle
        """

        empt_string = ""
        if self.__height == 0 or self.__width == 0:
            return (empt_string)
        for i in range(self.__height):
            empt_string += "#" * self.__width + '\n'
        return empt_string.rstrip()
