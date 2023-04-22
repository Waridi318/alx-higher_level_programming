#!/usr/bin/python3
"""
Defines a function that returns an object
(Python data structure) represented by a JSON string
"""

import json


def from_json_string(my_str):
    """
    function
    Args:
        my_str: JSON string
    Return: Py object
    """
    return(json.loads(my_str))
