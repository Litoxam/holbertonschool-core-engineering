#!/usr/bin/env python3
"""Read File"""


def read_file(filename=""):
    """function to read file"""
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")
