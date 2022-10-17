#!/usr/bin/python3
"""Rectangle module"""


class Rectangle():
    """The Rectangle Class"""

    def __init__(self, width=0, height=0):
        """initialize"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """width property"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """height property"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculate area"""
        return self.__height * self.__width

    def perimeter(self):
        """calculate perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """string representation"""
        if self.__height == 0 or self.__width == 0:
            return ""

        rep = ""
        for i in range(0, self.__height):
            rep += "#" * self.__width

            if i != self.__height - 1:
                rep += "\n"
        return rep

    def __repr__(self):
        """repr for rectangle"""
        return "Rectangle(" + str(self.__width) + ", "\
            + str(self.__height) + ")"

    def __del__(self):
        """on deletion"""
        print("Bye rectangle...")
