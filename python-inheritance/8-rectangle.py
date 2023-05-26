#!/usr/bin/python3
"""
Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).

Instantiation with width and height: def __init__(self, width, height):
width and height must be private. No getter or setter
width and height must be positive integers, validated by integer_validator
"""


class Rectangle(BaseGeometry):
    """This is a Rectangle class!"""
    def __init__(self, width, height):
        """This is the Initialization Method"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.width = __width
        self.height = __height
