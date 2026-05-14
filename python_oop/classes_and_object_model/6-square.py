#!/usr/bin/env python3
"""Implement instance methods."""


class Square:
    """Add getters and setters for the size attribute."""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def __str__(self):
        if self.__size == 0:
            return ""

        square = ""
        square += "\n" * self.__position[1]  # y

        for i in range(self.__size):  # x
            square += (" " * self.__position[0]) + ("#" * self.__size)
            if i < self.__size - 1:
                square += "\n"
        return square

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
        else:
            print(self)

    def area(self):
        return self.__size * self.__size

    def get_position(self):
        return self.__position

    def set_position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    size = property(get_size, set_size)
    position = property(get_position, set_position)


my_square = Square(5, (0, 0))
print(my_square)

print("--")

my_square = Square(5, (4, 1))
print(my_square)
