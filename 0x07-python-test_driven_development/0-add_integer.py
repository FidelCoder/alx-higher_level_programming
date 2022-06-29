#!/usr/bin/python3
"""
Module for adding two integers or floats
"""


def add_integer(a, b=98):
    """
    function that adds integers
    a and b must be integers or floats  
    a and b must be first casted to integers if they are float
    Returns an integer: the addition of a and b
    """
    if type(a) != int and type(a) != float or a is None:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
