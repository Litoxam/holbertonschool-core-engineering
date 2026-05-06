#!/usr/bin/env python3

def pow(a, b):
    """return the value of a raised to the power of b"""
    power = 1
    exponent = abs(b)
    if b == 0:
        return 1

    if b < 0:
        a = 1 / a

    for i in range(exponent):
        power *= a

    return power
