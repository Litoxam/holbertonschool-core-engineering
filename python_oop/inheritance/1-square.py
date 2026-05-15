#!/usr/bin/env python3
"""Introduction to Inheritance and Polymorphism"""


Rectangle = __import__('1-rectangle').Rectangle


class Square(Rectangle):
    """Create a class named Square, inherits from Rectangle"""
    def __init__(self, size):
        """Init Square, validate size"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Return the area of the Square"""
        return self.__size * self.__size

    def __str__(self):
        """Return the print() and str() representation of the Square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
