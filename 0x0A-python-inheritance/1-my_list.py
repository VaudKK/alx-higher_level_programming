#!/usr/bin/python3
""" my list module """


class MyList(list):
    """ my list class """
    def print_sorted(self):
        """ print sorted list"""
        print(sorted(self))
