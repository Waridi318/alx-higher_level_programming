#!/usr/bin/python3
"""
This module defines a function write_file
that writes a string to a text file
"""


def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF8)
    and returns the number of characters written

    Args:
        filename: name of file
        text: text to be written into file
    Return: number of characters written
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        return(f.write(text))
