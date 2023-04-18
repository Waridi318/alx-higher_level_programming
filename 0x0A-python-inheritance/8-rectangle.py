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
