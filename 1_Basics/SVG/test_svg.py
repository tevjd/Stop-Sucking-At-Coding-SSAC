#!/usr/bin/env python3
"""This is a test file for the SVG module"""

import svg

def test_svg_function():
    """Test if we can draw some circles in SVG format"""
    f = open("test_svg_circle.svg", "w", encoding="utf-8")
    f.write(svg.generate_start_tag_image(360, 340))
    f.write(svg.generate_start_tag_group("red", "black", 1))
    f.write(svg.generate_circle((50, 50), 20))
    f.write(svg.generate_end_tag_group())
    f.write(svg.generate_end_tag_image())
    f.close()

test_svg_function()
