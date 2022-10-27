#!/usr/bin/python3
""" write to file """
import json


def save_to_json_file(my_obj, filename):
    """ save json to file """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f, ensure_ascii=False)
