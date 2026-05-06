#!/usr/bin/env python3

for i in range(100):
    if i < 99:
        print("{:02d}".format(i), end=", ")
    else:
        print("{:02d}".format(i))
#  0 will fill the blank spaces, 2 is the width of our number
#  d is for the integer format
