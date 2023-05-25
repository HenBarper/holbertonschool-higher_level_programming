#!/usr/bin/python3
"""DOCUMENTED CODE IS HERE"""


class LockedClass:
    """DOCUMENTED CLASS IS HERE"""
    __slots__ = ['first_name']

    def __setattr__(self, attr, value):
        """SET THE ATTR BUT ONLY IS FIRST_NAME"""

        if not hasattr(self, attr) and attr != 'first_name':
            raise AttributeError("'LockedClass' object has \
no attribute '{}'".format(attr))
        super().__setattr__(attr, value)
