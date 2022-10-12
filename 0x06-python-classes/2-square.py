#!/usr/bin/python3
"""The square module"""


class Square:
    """Represents square"""

    def __init__(self, size):
        """Initialization of data"""
        if size < 0:
            raise ValueError('size must be >= 0')

        if type(size) != int:
            raise TypeError('size must be an integer')

        self.__size = size
