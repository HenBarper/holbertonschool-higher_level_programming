#!/usr/bin/python3
"""
Write a class Square that defines a square by: (based on 5-square.py)

Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it:
size must be an integer, otherwise raise a TypeError exception with a message
if size is less than 0, raise a ValueError exception
Private instance attribute: position:
property def position(self): to retrieve it
property setter def position(self, value): to set it:
position must be a tuple of 2 positive integers, otherwise raise a TypeError
Instantiation with optional size and optional position
Public instance method: def area(self): that returns the current square area
Public instance method: def my_print(self): that prints in stdout
if size is equal to 0, print an empty line
position  using space - Don’t fill lines by spaces when position[1] > 0
You are not allowed to import any module
"""


class Square:
    """This class defines a square with its size and position initialized"""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or value[0] <= 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int) or value[1] <= 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if self.__size <= 0:
            print()
        else:
            if self.__position[1] > 0:
                for _ in range(self.__position[1]):
                    print()
            for _ in range(self.__size):
                if self.__position[0] > 0:
                    print(" " * self.__position[0], end="")
                print("#" * self.__size)


my_square = Square(3, (1, -3))