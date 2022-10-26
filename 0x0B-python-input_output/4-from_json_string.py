#!/usr/bin/python3
"""" from json to string """
import json


def from_json_string(my_str):
    """ from json to string"""
    result = json.dumps(my_str)
    return result
