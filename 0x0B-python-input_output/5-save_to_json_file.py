#!/usr/bin/python3
"""Save JSON to file"""
import json


def save_to_json_file(my_obj, filename):
    """Writes json converted obj to file"""
    with open(filename, mode='w', encoding='utf-8') as fil:
        json.dump(my_obj, fil)
