#!/usr/bin/python3
"""Module 100-my_int.
Creates a class that inherits from int.
"""


class MyInt(int):
    """
    Reverses inequality and equality in int
    """

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
