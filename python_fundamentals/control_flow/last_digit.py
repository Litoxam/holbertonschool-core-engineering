#!/usr/bin/env python3

number = __import__('random').randint(-10000, 10000)

if number < 0:
    digit = number % -10
else:
    digit = number % 10

# to avoid typing the same thing 3 times
Message = f"Last digit of {number} is {digit}"

if digit > 5:
    print(f"{Message} and is greater than 5")
elif digit == 0:
    print(f"{Message} and is 0")
else:
    print(f"{Message} and is less than 6 and not 0")
