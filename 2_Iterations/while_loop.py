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

def gcd():
    """Compute the greatest common divisor"""

    val1 = int(input("Give us the first value: \n"))
    if val1 <= 0:
        raise ValueError("The value 1 need to be > 0 !")

    val2 = int(input("Give us the second value: \n"))
    if val2 <= 0:
        raise ValueError("The value 2 need to be > 0 !")

    while val1 != val2:
        if val1 < val2 :
            val2 -= val1
        else:
            val1 -= val2

    print("The result of the GCD is ", val1)

gcd()
