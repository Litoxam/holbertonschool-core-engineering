#!/usr/bin/env python3
"""Reinforce object modeling with a second class."""


class Rectangle:
    """Define a class Rectangle."""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def get_width(self):
        """returns the width"""
        return self.__width

    def set_width(self, value):
        """set new value to width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def get_height(self):
        """returns height"""
        return self.__height

    def set_height(self, value):
        """set new value to height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    width = property(get_width, set_width)
    height = property(get_height, set_height)
