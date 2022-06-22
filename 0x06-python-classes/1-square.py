#!/usr/bin/python3
"""
This module creates a class called square.
Private instance attribute: size
"""


class Square:
    """
    An empty class that defines a square
    Attributes:
        __size
    """

    def __init__(self, size):
        """
        __init__ method , during initialisation
        Args:
                size (no Type) : private size of square
        """
        self.__size = size
