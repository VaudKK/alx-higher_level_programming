#!/usr/bin/python3
""" My Int """


class MyInt(int):
    """ class my int """
    def __eq__(self, other):
        """ equal to """
        return not super().__eq__(other)

    def __ne__(self, other):
        """ not equal to """
        return not super().__ne__(other)
