#!/usr/bin/python3
"""
Unittesting for rectangle class
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    class for testing Rectangle class
    """
    def test_valid_attributes(self):
        '''test valid attribute values'''
        rectangle = Rectangle(10, 20, 5, 5)
        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.height, 20)
        self.assertEqual(rectangle.x, 5)
        self.assertEqual(rectangle.y, 5)

if __name__ == '__main__':
    unittest.main()
