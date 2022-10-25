#!/usr/bin/python3
""" add attribute module """


def add_attribute(clazz, name, value):
    """ add attribute """
    if type(clazz) in [int, str, list, float, dict, tuple, complex]:
        raise TypeError("can't add new attribute")

    if type(name) is not str:
        raise TypeError("can't add new attribute")

    setattr(clazz, name, value)
