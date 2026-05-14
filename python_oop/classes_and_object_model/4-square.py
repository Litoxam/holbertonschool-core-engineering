#!/usr/bin/env python3
"""Implement instance methods."""


class Square:
    """Add getters and setters for the size attribute."""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """return the area of square"""
        return self.__size * self.__size

    def get_size(self):
        """get the value of __size"""
        return self.__size

    def set_size(self, size):
        """set the private __size attribute"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
