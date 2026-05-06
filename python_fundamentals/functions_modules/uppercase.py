#!/usr/bin/env python3

def uppercase(str):
    """ print the string in uppercase followed by a new line"""
    for i in str:
        ascii_value = ord(i)
        if 97 <= ascii_value <= 122:
            print("{}".format(chr(ascii_value - 32)), end="")
        else:
            print("{}".format(i), end="")
    print("")
