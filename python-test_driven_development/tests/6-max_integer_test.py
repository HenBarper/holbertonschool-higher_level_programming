#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    class for testing 6-max_integer_test.py
    without arguments
    """
    def test_max_integer(self):
        """
        list of positive integers
        """
        test_list = [32, 5, 6, 12, 1, 17, 99]
        self.assertEqual(max_integer(test_list), 99)
