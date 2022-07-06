#!/usr/bin/python3
"""
Contains an empty class BaseGeometry
"""


class BaseGeometry():
    """
    Class on Geometry"""

    def area(self):
        """
        Raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates Integers
        """
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Inherits from class BaseGeometry
    """

    def __init__(self, width, height):
        """
        runs when class is initialised
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns area of rectangle
        """
        return self.__height * self.__width

    def __str__(self):
        """
        String representation of class
        """
        st = "[Rectangle] "
        st += str(self.__width)
        st += '/'
        st += str(self.__height)
        return st
