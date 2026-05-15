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
