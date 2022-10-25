#!/usr/bin/python3
""" square module """


class Square(__import__('9-rectangle').Rectangle):
    """ square class"""
    def __init__(self, size):
        """ initialize """
        Rectangle.__init__(self, size, size)
        self.__size = size

    def area():
        """ square area """
        return self.__size * self.__size
