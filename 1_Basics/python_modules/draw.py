#!/usr/bin/env python 3
"""Drawing module for the triangle"""

import random
import svg

def display_triangle(triangle, color):
    """
    This function display a triangle by outputing the svg code for
    transparent polygon
    """

    print(svg.generate_tag_start_group_transp(0.7))
    print(svg.generate_start_tag_group("none", color, 0))
    print(svg.generate_polygon(triangle))
    print(svg.generate_end_tag_group())
    print(svg.generate_end_tag_group())


def random_color():
    """Return a random color from all the possible color"""
    return f"#{random.randint(0, 0xFFFFFF):06x}"
