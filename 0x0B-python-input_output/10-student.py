#!/usr/bin/python3
"""Student class to dict"""


class Student():
    """A class of students"""

    def __init__(self, first_name, last_name, age):
        """Initializes class student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Obtain json representation of class"""
        dict2 = self.__dict__.copy()
        if type(attrs) is list and all(type(x) is str for x in attrs):
            delKey = []
            for key in dict2.keys():
                if key in attrs:
                    pass
                else:
                    delKey.append(key)
            for key in delKey:
                del dict2[key]
            return dict2
        else:
            return dict2
