#!/usr/bin/env python3
"""Introduction to Inheritance and Polymorphism"""


BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Create a class named Rectangle, inherits from BaseGeometry
    Both values are validated by the integer_validator
    """
    def __init__(self, width, height):
        """Init Rectangle, validate width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of the Rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
