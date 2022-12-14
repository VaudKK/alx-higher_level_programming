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
