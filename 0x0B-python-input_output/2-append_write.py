#!/usr/bin/python3
"""
This module defines a function append_write
that appends a string to the end of a text file
"""


def append_write(filename="", text=""):
    """
    writes a string to a text file (UTF8)
    and returns the number of characters written
    Args:
        filename: name of file
        text: text to be written into file
    Return: number of characters written
    """
    with open(filename, mode='a', encoding='utf-8') as f:
        return(f.write(text))
