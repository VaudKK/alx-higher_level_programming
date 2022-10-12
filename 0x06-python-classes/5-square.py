#!/usr/bin/python3
"""The square module"""


class Square:
    """Represents square"""

    def __init__(self, size=0):
        """Initialization of data"""
        if size < 0:
            raise ValueError('size must be >= 0')

        try:
            int(size)
        except TypeError:
            raise TypeError('size must be an integer')

        self.__size = size

    def area(self):
        """Get square"""
        return self.__size ** 2

    @property
    def size(self):
        """Getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter"""
        self.__size = value

    def my_print(self):
        """Print"""
        if self.__size > 0:
            for _ in range(0, self.__size):
                print("#" * self.__size)

        if self.__size == 0:
            print()
