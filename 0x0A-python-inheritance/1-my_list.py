#!/usr/bin/python3
"""
Has two classes . One inherits from the other
"""


class MyList(list):
    """
    Inherits properties from list
    """

    def print_sorted(self):
        """
        returns a sorted list
        """
        print(sorted(self))
