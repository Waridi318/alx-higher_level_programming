#!/usr/bin/python3
"""Module that defines a subclass
"""
from models.base import Base


class Rectangle(Base):
    """Child class from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""
        self.__width = width
        self.__height = height
        self.__x = x
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
        self.__x = x

    @property
    def y(self):
        """setter for y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """getter for y
        """
        self.__y = y
