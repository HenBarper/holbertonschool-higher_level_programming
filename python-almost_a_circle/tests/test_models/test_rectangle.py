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
    def test_auto_id_assign(self):
        """Auto assign ID exists"""
        r1 = Rectangle(1, 2)
        self.assertEqual(isinstance(r1, Rectangle), True)

if __name__ == '__main__':
    unittest.main()
