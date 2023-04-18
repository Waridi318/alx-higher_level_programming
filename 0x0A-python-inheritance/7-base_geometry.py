#!/usr/bin/python3
"""
This module defines an empty class
"""


class BaseGeometry:
    """
    This is a class BaseGeometry.
    """
    def area(self):
        """Public instance method
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method that validates value
        """
        if type(value) is not (int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
