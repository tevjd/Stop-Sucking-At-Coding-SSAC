#!/usr/bin/env python3
"""Kaleidoscope program"""

import sys
from math import pi
import svg
import draw
from triangle import random_triangle, turn_triangle_around

def generate_image(number_of_triangle):
    """
    Function that generate the triangles randomly and turn them.
    It generates the SVG code on the sysout
    """
    wide, height = 800.0, 600.0
    print(svg.generate_start_tag_image(wide, height))
    center = (wide/2, height/2)

    for _ in range(number_of_triangle):
        #we generate the first triangle in the right below quarter
        triangle = random_triangle((wide/2, wide), (height/2, height))
        color = draw.random_color()
        #we turn the triangle to dipslay it height times
        for i in range(8):
            angle = pi / 4 * i
            turned_triangle = turn_triangle_around(triangle, center, angle)
            draw.display_triangle(turned_triangle, color)

    print(svg.generate_end_tag_image())


def main():
    """Main function of the program that proceed the command line"""

    if len(sys.argv) != 2 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print("Usage: ./", sys.argv[0], " number of triangle > image.svg")
        sys.exit(1)

    number_of_triangle = int(sys.argv[1])
    generate_image(number_of_triangle)


if __name__ == "__main__":
    main()
