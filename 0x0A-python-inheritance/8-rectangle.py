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
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Represents a rectangle.
    Private instance attributes:
        - width
        - height
    Inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """Initializes an instance.
        Args:
            - width: width of the rectangle
            - heigth: height of the rectangle
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
