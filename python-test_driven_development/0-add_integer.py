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

    if a is None or type(a) not in [int, float] or a is not a or abs(a) > 1.7976931348623158e+308:
        raise TypeError("a must be an integer")
    if b is None or type(b) not in [int, float] or b is not b or abs(b) > 1.7976931348623158e+308:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
