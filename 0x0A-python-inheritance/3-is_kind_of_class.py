#!/usr/bin/python3
"""
This module defines a function
"""


def is_kind_of_class(obj, a_class):
    """
    returns True if the object is an instance of,
    or if the object is an instance of a class that
    inherited from, the specified class ; otherwise False

    Args:
        obj: object
        a_class: class
    Return:
        True if isinstance, else False
    """
    return isinstance(obj, a_class)
