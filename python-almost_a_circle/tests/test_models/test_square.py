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
    def test_valid_attributes_1(self):
        """test valid attribute values x1"""
        square = Square(99)
        self.assertEqual(square.size, 99)

    def test_valid_attributes_2(self):
        """test valid attribute values x2"""
        square = Square(50, 1)
        self.assertEqual(square.size, 50)
        self.assertEqual(square.x, 1)

    def test_valid_attributes_3(self):
        """test valid attribute values x3"""
        square = Square(25, 2, 3)
        self.assertEqual(square.size, 25)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_valid_attributes_4(self):
        """test valid attribute values x4"""
        square = Square(25, 2, 3, 99)
        self.assertEqual(square.size, 25)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 99)

    def test_invalid_size(self):
        """test invalid size values"""
        with self.assertRaises(TypeError):
            Square("string")

    def test_invalid_x(self):
        """test invalid x values"""
        with self.assertRaises(TypeError):
            Square(2, "string")

    def test_invalid_y(self):
        """test invalid y values"""
        with self.assertRaises(TypeError):
            Square(2, 1, "string")

    def test_negative_size(self):
        """test invalid negative size"""
        with self.assertRaises(ValueError):
            Square(-5)

    def test_negative_x(self):
        """test invalid negative x"""
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_negative_y(self):
        """test invalid negative y"""
        with self.assertRaises(ValueError):
            Square(1, 2, -4)

    def test_zero_size(self):
        """test zero size"""
        with self.assertRaises(ValueError):
            Square(0)

    def test_str(self):
        s1 = Square(5, 2, 3, 99)
        self.assertEqual(str(s1), "[Square] (99) 2/3 - 5")

if __name__ == '__main__':
    unittest.main()
