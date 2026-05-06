#!/usr/bin/env python3

def uppercase(str):
    """ print the string in uppercase followed by a new line"""
    for char in str:
        ascii_value = ord(char)  # Get the ascii value of each char

        if 97 <= ascii_value <= 122:
            print("{}".format(chr(ascii_value - 32)), end="")
        else:
            print("{}".format(char), end="")
    print("")
