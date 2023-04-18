#!/usr/bin/python3
"""
This module defines parent and child classes
"""


class MyList(list):
    """
    child class
    """
    def print_sorted(self):
        """
        prints list, but sorted
        """
        print(sorted(self))
