#!/usr/bin/python3
"""Module that reads files"""


def read_file(filename=""):
    """Reads all contexts of a file and prints"""
    with open(filename, encoding="utf-8") as fil:
        x = fil.read()
        print(x, end="")
