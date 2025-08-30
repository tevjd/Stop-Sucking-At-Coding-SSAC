#!/usr/bin/env python3
"""This is a module to proceed triangle form"""

import sys
import random
from math import cos, sin


def random_triangle(x_range, y_range):
    """
    This function take the coordonate of begining and end.
    And return a random triangle with 3 points in the area 
    define by the points in parameters
    """
    coordinate = []
    for _ in range(3):
        x_1 = random.randint(x_range[0], x_range[1])
        y_1 = random.randint(y_range[0], y_range[1])
        coordinate.append((x_1, y_1))

    return coordinate

def turn_triangle_around(triangle, center, angle):
    """
    Function that turn all the coordinate of a triangle
    """
    turned_coordinate = []
    for x_b, y_b in triangle:
        x_c = (x_b - center[0])*cos(angle) - (y_b - center[1])*sin(angle) + center[0]
        y_c = (x_b - center[0])*sin(angle) + (y_b - center[1])*cos(angle) + center[1]

        turned_coordinate.append((x_c, y_c))

    return turned_coordinate

def main():
    """Main function"""
    sys.exit(0)

if __name__ == "__main__":
    main()
