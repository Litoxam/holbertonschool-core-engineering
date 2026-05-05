#!/usr/bin/env python3

def islower(c):
    """returns True if c is a lowercase letter and False otherwise."""
    if 97 <= ord(c) <= 122:
        return True
    else:
        return False
