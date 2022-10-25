#!/usr/bin/python3
""" base geometry """


class BaseGeometry():
    """ base geo class"""

    def area(self):
        """ get area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validate integer """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
