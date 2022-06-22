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

    def __init__(self, size=0, position=(0, 0)):
        """
        __init__ method , during initialisation
        Args:
                size (int) : private size of square default value of 0.
                position (tuple)
        """
        lds = position
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position[0], int) or not isinstance(lds[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__size = size
            self.__position = position

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

    @property
    def position(self):
        """"
        getter that returns the position the square should be plotted
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter that changes the value of position
        Attributes:
                value(tuple): new value of position
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        plots the square using # as a place holder
        attrributes:
                __size
                __position
                i
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print("{}{}".format(' '*self.__position[0], '#'*self.__size))
