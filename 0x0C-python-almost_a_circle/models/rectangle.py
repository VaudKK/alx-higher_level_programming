#!/usr/bin/python3
""" rectangle module """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize """
        super().__init__(id)

        if type(width) is not int:
            raise TypeError("width must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")

        if type(height) is not int:
            raise TypeError("height must be an integer")

        if height <= 0:
            raise ValueError("height must be > 0")

        if type(x) is not int:
            raise TypeError("x must be an integer")

        if x < 0:
            raise ValueError("x must be >= 0")

        if type(y) is not int:
            raise TypeError("y must be an integer")

        if y < 0:
            raise ValueError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ getter width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter width """
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """ get height """
        return self.__height

    @height.setter
    def height(self, value):
        """ set height """
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """ get x """
        return self.__x

    @x.setter
    def x(self, value):
        """ set x """
        if type(value) is not int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """ get y"""
        return self.__y

    @y.setter
    def y(self, value):
        """ set y """
        if type(value) is not int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """ returns the area """
        return self.__width * self.__height

    def display(self):
        """ display rectangle """
        for _ in range(0, self.__y):
            print("")

        for _ in range(0, self.__height):
            for _ in range(0, self.__x):
                print(" ", end='')
            print("#" * self.__width)

    def __str__(self):
        """ ovr str """
        return "[Rectangle] ({}) {}/{} - {}/{}"\
               .format(self.id, self.__x, self.__y,
                       self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ update rectangle values """
        my_attr = ["id", "width", "height", "x", "y"]
        if args is not None:
            for index in range(0, len(args)):
                setattr(self, my_attr[index], args[index])

        if kwargs is not None:
            for key, value in kwargs.items():
                if key in my_attr:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ to dictionary """
        return {'id': self.id, 'width': self.__width, 'height': self.__height,
                'x': self.__x, 'y': self.__y}
