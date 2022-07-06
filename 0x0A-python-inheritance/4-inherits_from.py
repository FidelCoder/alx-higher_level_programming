#!/usr/bin/python3
"""
Module which has function that checks
if instance is a subclass of certain class
"""


def inherits_from(obj, a_class):
    """
    Checks if obj has inherited from a_class
    """
    if isinstance(obj, a_class):
        if type(obj) == a_class:
            return False
        else:
            return True
    else:
        return False
