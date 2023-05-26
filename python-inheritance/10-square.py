#!/usr/bin/python3
"""
Write a class Square that inherits from Rectangle (9-rectangle.py):

Instantiation with size: def __init__(self, size)::
size must be private. No getter or setter
size must be a positive integer, validated by integer_validator
the area() method must be implemented
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """This is the Initialization Method"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """returns area of square"""
        return (self.__size ** 2)

    def __str__(self):
        """return string representation of rectangle"""
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
