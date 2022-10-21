#!/usr/bin/python3
""" square module """


def print_square(size):
    """ print a square """
    if type(size) is float and size < 0:
        raise TypeError('size must be an integer')

    if type(size) is not int:
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    for _ in range(0, size):
        print('#' * size)
