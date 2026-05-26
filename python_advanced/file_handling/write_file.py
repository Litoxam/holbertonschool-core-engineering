#!/usr/bin/env python3
"""Write File"""


def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF-8) and returns the number
    of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
