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
