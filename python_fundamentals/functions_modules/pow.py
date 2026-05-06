#!/usr/bin/env python3

def pow(a, b):
    """return the value of a raised to the power of b"""
    if b == 0:
        return 1
    
    power = a
    for i in range(b - 1):
        power *= a
    print("{}".format(power))

    return (power)
