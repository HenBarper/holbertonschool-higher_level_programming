#!/usr/bin/python3
"""
A class Rectangle that defines a rectangle by:

Private instance attribute: width:
property def width(self): to retrieve it
property setter def width(self, value): to set it:
width must be an integer
if width is less than 0, raise a ValueError
Private instance attribute: height:
property def height(self): to retrieve it
property setter def height(self, value): to set it:
height must be an integer
if height is less than 0, raise a ValueError
Instantiation = def __init__(self, width=0, height=0):
def area(self): that returns the rectangle area
def perimeter(self): that returns the rectangle perimeter:
if width or height is equal to 0, perimeter is equal to 0
print() and str() should print the rectangle with the character #:
if width or height is equal to 0, return an empty string
repr() should return a string representation of the rectangle
    to be able to recreate a new instance by using eval()
Print the message Bye rectangle... (... being 3 dots not ellipsis)
    when an instance of Rectangle is deleted
Public class attribute number_of_instances:
    Initialized to 0
    Incremented during each new instance instantiation
    Decremented during each instance deletion
Public class attribute print_symbol:
    Initialized to #
    Used as symbol for string representation
    Can be any type
Static method def bigger_or_equal(rect_1, rect_2):
    that returns the biggest rectangle based on the area
rect_1 must be an instance of Rectangle, otherwise raise a TypeError
    exception with the message rect_1 must be an instance of Rectangle
rect_2 must be an instance of Rectangle, otherwise raise a TypeError
    exception with the message rect_2 must be an instance of Rectangle
Returns rect_1 if both have the same area value
"""


class Rectangle:
    """Rectangle class"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initialization method for the Rectangle class

        Attributes:
            width: Width of rectangle
            height: Height of rectangle
        self.width = width
        self.height = height
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Property width to retrieve it

        Returns:
            width: Width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter width of the rectangle

        Attributes:
            width: Width of rectangle

        Raises:
            TypeError: If width is not an integer
            ValueError: If width is less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Property height to retrieve it

        Returns:
            height: Height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter height of the rectangle

        Attributes:
            height: height of rectangle

        Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Return the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.width > 0 and self.height > 0:
            return (self.width * 2) + (self.height * 2)
        else:
            return 0

    def __str__(self):
        """Prints string representation of rectangle"""
        string = ""
        if self.width > 0 and self.height > 0:
            for row in range(self.height):
                for col in range(self.width):
                    string += str(self.print_symbol)
                if row < self.height - 1:
                    string += '\n'
            return string
        else:
            return string

    def __repr__(self):
        """Return literal string representation"""
        return "Rectangle(" + str(self.__width) + ", " + str(self.__height) +\
            ")"

    def __del__(self):
        """Prints after deletion"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("Rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("Rect_2 must be an instance of Rectangle")
        area_1 = rect_1.area()
        area_2 = rect_2.area()
        if area_1 > area_2 or area_1 == area_2:
            return rect_1
        elif area_1 < area_2:
            return rect_2
