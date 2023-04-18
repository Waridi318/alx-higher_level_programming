#!/usr/bin/python3
def is_same_class(obj, a_class):
    """
    checks if obj is an instance of a_class

    Args:
        obj: object
        a_class: class
    Return:
        True if isinstance, else False
    """
    if isinstance(obj, a_class):
        return True
    else: 
        return False
