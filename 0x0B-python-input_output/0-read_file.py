#!/usr/bin/python3
""" read something """


def read_file(filename=""):
    """" read a file """
    with open(filename, encoding='utf-8') as f:
        read_data = f.read()
        print(read_data, end='')
