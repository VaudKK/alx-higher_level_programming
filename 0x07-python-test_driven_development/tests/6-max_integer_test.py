#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        """ test empty list"""
        self.assertEqual(max_integer([]),None)

    def test_list_with_non_integer(self):
        """ test non integer values """
        self.assertRaises(TypeError, max_integer, [4,5,6,'a',8])

    def test_max_value(self):
        """ test for max value"""
        self.assertEqual(max_integer([6,7,8,9]),9)
