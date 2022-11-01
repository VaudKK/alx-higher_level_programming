#!/usr/bin/python3
""" square module """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Rectangle class """
    def __init__(self, size, x=0, y=0, id=None):
        """ initialize """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ to string """
        return "[Square] ({}) {}/{} - {}"\
               .format(self.id, self.x, self.y,
                       self.width)

    @property
    def size(self):
        """ get size """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value
