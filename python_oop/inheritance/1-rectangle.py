#!/usr/bin/env python3
"""Introduction to Inheritance and Polymorphism"""


class BaseGeometry:
    """Create a class named BaseGeometry"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if (not isinstance(value, int) or
                type(value) is bool):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        return value


class Rectangle(BaseGeometry):
    """Create a class named Rectangle, inherits from BaseGeometry
    Both values are validated by the integer_validator
    """
    def __init__(self, width, height):

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
