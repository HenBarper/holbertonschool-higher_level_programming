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
        self.assertEqual(b1.id, 1)
