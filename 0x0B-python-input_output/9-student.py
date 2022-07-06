#!/usr/bin/python3
"""Student class to dict"""


class Student():
    """A class of students"""

    def __init__(self, first_name, last_name, age):
        """Initializes class student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Obtain json representation of class"""
        return self.__dict__
