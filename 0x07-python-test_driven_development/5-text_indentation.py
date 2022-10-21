#!/usr/bin/python3
""" string tings"""


def text_indentation(text):
    """indent text"""
    if type(text) is not str:
        raise TypeError('text must be a string')

    new_string = ""
    for c in text:
        if c in ['.', '?', ':']
            new_string += c
            new_string += '\n\n'
        elif c != ' ':
            new_string += c

    print(new_string)
