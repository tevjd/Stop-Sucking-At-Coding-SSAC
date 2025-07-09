#!/usr/bin/env python3
"""This is a file to understand how to use the arguments in python"""

import sys

def test_argv():
    """Function that needs an arguments"""

    if len(sys.argv) == 1:
        print(f"Here is how to use the program: ./{sys.argv[0]} arg1 arg2 ... argN")
        sys.exit(0)

    for elem in sys.argv:
        print(elem)


if __name__ == "__main__":
    test_argv()
