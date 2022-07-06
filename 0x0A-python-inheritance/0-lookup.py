#!/usr/bin/python3
"""
Module that contains function that returns attrributes
and methods of an object
"""


def lookup(obj):
    """
    returns list of all attributes and methods of obj
    """
    return dir(obj)
