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

    def get_size(self):
        """get the value of __size"""
        return self.__size

    def set_size(self, new_size):
        if not isinstance(new_size, int):
            raise TypeError("size must be an integer")
        if new_size < 0:
            raise ValueError("size must be >= 0")
        self.__size = new_size

    def my_print(self):
        if self.size == 0:  # size -> property -> get_size -> value
            print()
            return
        for i in range(self.size):
            print("#" * self.size)

    def area(self):
        return self.__size * self.__size

    size = property(get_size, set_size, my_print)
