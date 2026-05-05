#!/usr/bin/env python3

for i in range(9):  # i goes from 0 to 8
    for j in range(i + 1, 10):  # j goes from 1 to 9
        if i == 8 and j == 9:
            print("{}{}".format(i, j))
        else:
            print("{}{}".format(i, j), end=", ")
