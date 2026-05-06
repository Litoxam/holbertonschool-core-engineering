#!/usr/bin/env python3

def pow(a, b):
    """return the value of a raised to the power of b"""
    if b == 0:
        print(1)
        return 1
    
    power = 1
    for i in range(b):
        power *= a
    print("{}".format(power))
    return power
