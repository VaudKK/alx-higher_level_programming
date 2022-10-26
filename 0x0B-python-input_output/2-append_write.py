#!/usr/bin/python3
""" append to file """


def append_write(filename="", text=""):
    """ append to a file """
    with open(filename, 'a', encoding='utf-8') as f:
        written = f.write(text)
        return written
