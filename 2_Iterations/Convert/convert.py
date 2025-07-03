#!/usr/bin/env python3
"""This is a program to convert points in a txt file in an SVG image"""

import svg

def main():
    """
    Main function that takes an input of points (one coordinate on each line).
    And create an SVG image with all the points
    """

    print(svg.generate_start_tag_image(640, 480))
    print(svg.generate_start_tag_group('black', 'black', 1))

    try:
        while True:
            point_x = int(input())
            point_y = int(input())

            print(svg.generate_circle((point_x, point_y), 1))

    except EOFError:
        pass

    print(svg.generate_end_tag_group())
    print(svg.generate_end_tag_image())

if __name__ == "__main__":
    main()
