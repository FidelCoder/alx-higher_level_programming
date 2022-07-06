#!/usr/bin/python3
"""
Contains function that checks if an istance is of exact certain class
"""


def is_same_class(obj, a_class):
    """
    Check if object is of a_class
    """
    if type(obj) == a_class:
        return True
    else:
        return False
