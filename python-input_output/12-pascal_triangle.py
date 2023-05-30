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
    temp_list = []
    final_list = []

    for i in range(n):
        new_list = temp_list[:]
        new_list.append(1)
        for i in range(1, len(temp_list)):
            new_list[i] = temp_list[i - 1] + temp_list[i]
        temp_list = new_list[:]
        final_list.append(temp_list)
    return final_list
