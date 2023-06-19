#!/usr/bin/python3
"""
This module defines a function is_same_class
"""


def is_same_class(obj, a_class):
    """
    checks if obj is an instance of a_class

    Args:
        obj: object
        a_class: class
    Return:
        True if isinstance, else False
    """
    return type(obj) == a_class
