#!/usr/bin/python3
""" load and save """
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


filename = "add_item.json"
all_arguments = []

try:
    all_arguments = load_from_json_file(filename)
except Exception as e:
    pass

all_arguments += [x for x in sys.argv[1:]]
save_to_json_file(all_arguments, "add_item.json")
