#!/usr/bin/python3
"""
This module defines a function that returns
JSON representation of an object
"""
import json


def to_json_string(my_obj):
    """
    returns the JSON representation of an object (string)

    Args:
        my_obj: object
    Returns: JSON representation
    """
    new_obj = json.dumps(my_obj)
    return new_obj
