#!/usr/bin/python3
""" returns the JSON representation of an object (string)"""
import json


def to_json_string(my_obj):
    """ returns JSON of object"""
    return json.dumps(my_obj)
