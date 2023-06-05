#!/usr/bin/python3
"""
Unittesting for rectangle class
"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    class for testing Rectangle class
    """
    def test_valid_attributes_2(self):
        '''test valid attribute values x1'''
        square = Square(10)
        self.assertEqual(square.size, 10)

if __name__ == '__main__':
    unittest.main()
