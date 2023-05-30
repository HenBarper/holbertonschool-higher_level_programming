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
    new_list = []
    temp_list = []

    for i in len(n):
        temp_list = []
        templist.append(1)
        if i > 1:
            for j in len(i):
                templist.append(new_list[i][j] + new_list[i][j + 1])
                new_list.append(temp_list)

                return new_list
