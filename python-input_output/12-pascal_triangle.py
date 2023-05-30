#!/usr/bin/python3
"""
You are not allowed to google anything
Whiteboard first
Create a function def pascal_triangle(n): that
returns a list of lists of integers representing
    the Pascal’s triangle of n:

Returns an empty list if n <= 0
You can assume n will be always an integer
You are not allowed to import any module
"""


def pascal_triangle(n):
    """func to return list of lists for n in pascals triangle"""
    pascal = []
    triangle = []

    for i in range(int(n)):
        new = pascal[:]
        new.append(1)
        pos = len(pascal)
        for i in range(1, pos):
            new[i] = pascal[i - 1] + pascal[i]
        pascal = new[:]
        triangle.append(pascal)
    return triangle
