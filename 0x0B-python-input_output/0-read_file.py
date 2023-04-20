#!/usr/bin/python3
"""
This module describes a function that reads a file
"""


def read_file(filename=""):
    """
    reads a text file and prints it to stdout
    """
    with open(filename, encoding='utf-8') as f:
        return(f.read())
