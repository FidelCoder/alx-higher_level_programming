#!/usr/bin/python3
"""
Interchanges equal sign of int
"""


class MyInt(int):
    def __eq__(self, other):
        """
        not equal function returns true
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        equal function returns true
        """
        return super().__eq__(other)
