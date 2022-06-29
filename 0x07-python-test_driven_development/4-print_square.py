#!/usr/bin/python3
"""
module contains function that prints a square of #
"""


def print_square(size):
    """
    function that prints square according to size passed
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("{}".format('#'*size))
    if size == 0:
        print()
