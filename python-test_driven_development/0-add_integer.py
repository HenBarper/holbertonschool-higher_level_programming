#!/usr/bin/python3
""" 0. Integers Addition - 0-add_integer.py """


def add_integer(a, b=98):
    """
    This function adds two integers
    or floats casted to int

    Args:
        a: first integer to add
        b: second iteger to add

    Raises:
        TypeError if a or b is not float or int

    Return:
        The result of the operation
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
