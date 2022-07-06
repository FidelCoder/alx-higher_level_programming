#!/usr/bin/python3
"""creates an Object from a “JSON file"""
import json


def load_from_json_file(filename):
    """reads and creates obj from JSON"""
    with open(filename, mode='r', encoding='utf-8') as fil:
        return json.load(fil)
