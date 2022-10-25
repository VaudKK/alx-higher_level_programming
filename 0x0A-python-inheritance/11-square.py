#!/usr/bin/python3
""" square module """


class Square(__import__('9-rectangle').Rectangle):
    """ square class"""
    def __init__(self, size):
        """ initialize """
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ square area """
        return self.__size ** 2

    def __str__(self):
        """ str() """
        return "[Square] {}/{}".format(self.__size, self.__size)

    def __repr__(self):
        """ to string """
        return "[Square] {}/{}".format(self.__size, self.__size)
