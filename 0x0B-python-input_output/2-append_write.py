#!/usr/bin/python3
"""Module that appens a file"""


def append_write(filename="", text=""):
    """Appends text to a file"""
    with open(filename, mode='a', encoding='utf-8') as fil:
        x = fil.write(text)
    return x
