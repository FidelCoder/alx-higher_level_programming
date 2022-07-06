#!/usr/bin/python3
"""appends after a certain string"""


def append_after(filename="", search_string="", new_string=""):
    """"append new string after key word"""
    str = ''
    with open(filename, mode='r', encoding='utf-8') as file:
        for line in file:
            str += line
            if search_string in line:
                str += new_string

    with open(filename, mode='w', encoding='utf-8') as file:
        x = file.write(str)
