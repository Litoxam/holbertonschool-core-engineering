#!/usr/bin/env python3

def uppercase(str):
    """print the string in uppercase followed by a new line"""
    result = ""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            result += chr(ord(char) - 32)
        else:
            result += char
    print("{}".format(result))
