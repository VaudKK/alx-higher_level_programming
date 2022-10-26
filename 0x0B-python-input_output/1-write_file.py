#!/usr/bin/python3
""" write to file """


def write_file(filename="", text=""):
    """ write to file """
    with open(filename, 'w', encoding='utf-8') as f:
        written = f.write(text)
        return written
