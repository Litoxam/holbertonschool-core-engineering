#!/usr/bin/env python3

def uppercase(str):
    """ print the string in uppercase followed by a new line"""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            print(chr(ord(char) - 32), end="")
        else:
            print(char, end="")
    print("")
