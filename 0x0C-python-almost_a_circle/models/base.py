#!/usr/bin/python3
"""
This module defines a class Base
"""


class Base:
    """
    This ia a base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        This is a class constructor
        """
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
