#!/usr/bin/python3

"""Module that defines a subclass
"""
from models.base import Base


class Rectangle(Base):
    """Child class from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""
        if type(width) is not (int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width
        if type(height) is not (int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height
        if type(x) is not (int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x
        if type(y) is not (int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

        super().__init__(id)

    @property
    def width(self):
        """getter for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """set the width attribute
        """
        if type(value) is not (int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """gets the height attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """set the height attribute
        """

        if type(value) is not (int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """getter for x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x
        """
        if type(value) is not (int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """setter for y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """getter for y
        """
        if type(value) is not (int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Public method
        """
        return self.__height * self.__width

    def display(self):
        """
        prints rectangle to stdout"""
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            print()
