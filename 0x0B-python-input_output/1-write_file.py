#!/usr/bin/python3
"""Module that writes to a file"""


def write_file(filename="", text=""):
    """Writes text to a file"""
    with open(filename, mode='w', encoding='utf-8') as fil:
        x = fil.write(text)
    return x
