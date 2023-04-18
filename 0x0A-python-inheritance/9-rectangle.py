#!/usr/bin/python3
"""
This module defines a subclass of the BaseGeometry class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This is a subclass of BaseGeometry
    """
    def __init__(self, width, height):
        """Constructor of Rectangle
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        defines public instance method area
        """
        return(self.__width * self.__height)

    def __str__(self):
        """return string representation
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
