#!/usr/bin/env python3
"""Program to play with some function of the random module"""

import random


def main():
    """This is the main function. We will play with randint() and choice()."""

    # Generate a list with 100 random number between 0 and 1000 included
    my_random = [random.randint(0, 1000) for _ in range(100)]

    print(my_random)

    for _ in range(10):
        print(f"Here is one element of the list chose randomly : {random.choice(my_random)}")


if __name__ == "__main__":
    main()
