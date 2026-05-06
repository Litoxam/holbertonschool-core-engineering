#!/usr/bin/env python3

import calculator_1


def addition():
    a = 10
    b = 5
    result = calculator_1.add(a, b)
    print("{} + {} = {}".format(a, b, result))


def substraction():
    a = 10
    b = 5
    result = calculator_1.sub(a, b)
    print("{} + {} = {}".format(a, b, result))


def multiplication():
    a = 10
    b = 5
    result = calculator_1.mul(a, b)
    print("{} + {} = {}".format(a, b, result))


def division():
    a = 10
    b = 5
    result = calculator_1.div(a, b)
    print("{} + {} = {}".format(a, b, result))


if __name__ == "__main__":
    addition()
    substraction()
    multiplication()
    division()
