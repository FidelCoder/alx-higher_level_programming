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

    def __init__(self, size=0):
        """
        __init__ method , during initialisation
        Args:
                size (int) : private size of square default value of 0.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculates Area of square
        Uses __size attribute
        Returns:
                Area of square
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        A getter used to access private instance size
        Returns:
                size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        size setter  method , changes value of size
        Args:
                value (int) : private size of square default value of 0.
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """
        plots the square using # as a place holder
        attrributes:
                _size
                i
        """
        for i in range(self.__size):
            print("{}".format('#'*self.__size))
        if (self.__size == 0):
            print()
