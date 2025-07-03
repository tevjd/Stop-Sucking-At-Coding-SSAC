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

a_string = "123"
a_list = [1, 2, 3]
a_tuple = (1, 2, 3)
a_2D_tuple = ([1, 2, 3], [4, 5, 6])
a_3D_tuple = [[[1, 2], [3, 4]], [[5, 6]]]

def go_through(data_structure):
    """Function that will print all the element of the data structure"""

    print(f"Elements of the structure {data_structure}")
    stack = [data_structure]

    while stack :
        elem = stack.pop()

        if isinstance(elem, str):
            for letter in elem:
                print(letter)

        elif isinstance(elem, (list, tuple)):
            i = len(elem) - 1
            while i >= 0 :
                stack.append(elem[i])
                i -= 1

        else:
            print(elem)

go_through(a_string)
go_through(a_list)
go_through(a_tuple)
go_through(a_2D_tuple)
go_through(a_3D_tuple)
