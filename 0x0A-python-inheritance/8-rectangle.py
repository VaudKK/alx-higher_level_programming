#!/usr/bin/python3
""" rectangle module """


class Rectangle(__import__('7-base_geometry').BaseGeometry):
    """ rectangle class"""
    def __init__(self, width, height):
        """ initialize """
        Rectangle.integer_validator(self, "width", width)
        Rectangle.integer_validator(self, "height", height)

        self.__width = width
        self.__height = height
