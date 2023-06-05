#!/usr/bin/python3
"""
Unittesting time is now
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    class for testing Base class
    """
    def test_auto_id_assign(self):
        """Auto assign ID exists"""
        b1 = Base()
        b2 = Base()
        b3 = Base(99)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 99)
