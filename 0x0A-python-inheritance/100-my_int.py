#!/usr/bin/python3
"""
This module defines a class MyInt
"""


class MyInt(int):
    """
    This is MyInt class, subclass of int
    """
    def __eq__(self, other):
        """checks for equality and reverses the expected output
        """
        return (int(self) != int(other))

    def __ne__(self, other):
        """
        checks for inequality and reverses the expacted output
        """
        return (int(self) == int(other))
