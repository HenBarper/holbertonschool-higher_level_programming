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
    def test_valid_attributes_2(self):
        '''test valid attribute values x2'''
        rectangle = Rectangle(10, 99)
        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.height, 99)

    def test_valid_attributes_4(self):
        '''test valid attribute values x4'''
        rectangle = Rectangle(10, 20, 5, 5)
        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.height, 20)
        self.assertEqual(rectangle.x, 5)
        self.assertEqual(rectangle.y, 5)

    def test_valid_attributes_5(self):
        '''test valid attribute values x5'''
        rectangle = Rectangle(10, 20, 5, 5, 99)
        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.height, 20)
        self.assertEqual(rectangle.x, 5)
        self.assertEqual(rectangle.y, 5)
        self.assertEqual(rectangle.id, 99)

    def test_invalid_width(self):
        '''test invalid width values'''
        with self.assertRaises(TypeError):
            Rectangle("string", 20, 5, 5)

    def test_invalid_height(self):
        '''test invalid height values'''
        with self.assertRaises(TypeError):
            Rectangle(20, "string", 5, 5)

    def test_invalid_x(self):
        '''test invalid x values'''
        with self.assertRaises(TypeError):
            Rectangle(5, 20, "string", 5)

    def test_invalid_y(self):
        '''test invalid y values'''
        with self.assertRaises(TypeError):
            Rectangle(5, 20, 99, "string")

if __name__ == '__main__':
    unittest.main()
