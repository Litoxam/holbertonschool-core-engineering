#!/usr/bin/env python3
"""Introduce instance attributes."""


class Square:
    """Add validations to the sizeattribute on the Square class"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
