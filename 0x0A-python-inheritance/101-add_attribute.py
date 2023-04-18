#!/usr/bin/python3
"""
This module defines a function add_attribute
"""


def add_attribute(a, b, c):
    """
    This function adds a new attribute to an object if it’s possible
    Args:
        a: object
        b: name of attribute
        c: value of attribute
    """
    if not hasattr(a, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(a, b, c)
