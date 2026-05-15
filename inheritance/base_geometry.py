#!/usr/bin/env python3
"""Introduction to Inheritance and Polymorphism"""


class BaseGeometry:
    """Create a class named BaseGeometry"""
    def __init__(self, name="", value=0):
        self.name = name
        self.value = value

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
