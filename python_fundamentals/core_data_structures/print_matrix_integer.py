#!/usr/bin/env python3


def print_matrix_integer(matrix=[[]]):
    """prints a matrix of integers"""
    for line in matrix:
        for col in range(len(line)):
            print("{:d}".format(line[col]), end="")
            if col < len(line) - 1:
                print(" ", end="")

        print()
