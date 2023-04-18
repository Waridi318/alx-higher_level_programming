#!/usr/bin/python3
"""
This module defines a function inherits_from
"""


def inherits_from(obj, a_class):
    """
    checks if obj is a subclass of class
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
