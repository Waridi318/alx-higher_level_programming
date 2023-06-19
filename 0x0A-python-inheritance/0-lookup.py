#!/usr/bin/python3
"""
This is a module for the function lookup
"""


def lookup(obj):
    """
    Function that checks available
    attributes and methods of an object

    Args:
        obj (object): param

    Returns:
        list object
    """

    return (dir(obj))
