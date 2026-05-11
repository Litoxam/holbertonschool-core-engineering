#!/usr/bin/env python3

def safe_print_integer(value):
    """prints an integer with "{:d}".format() followed by a new line"""
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
