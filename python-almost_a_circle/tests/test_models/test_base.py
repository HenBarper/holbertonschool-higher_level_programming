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
    def auto_id_assign(self):
        """Auto assign ID exists"""
        b1 = Base()
        the_id = b1.id
        self.assertEqual(the_id, 1)
