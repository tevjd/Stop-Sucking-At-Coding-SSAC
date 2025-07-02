#!/usr/bin/env python3
"""This is a python program to learn about while loop"""


def factorial():
    """Return the result of a factorial value: val!"""

    val = int(input("Give me a number: \n"))
    if val < 0:
        raise ValueError("You can only give an integer >= 0.")

    result = 1
    while val > 1:
        result *= val
        val -= 1

    print(f"The result is {result}")

factorial()
