#!/usr/bin/env python3
"""
This is a snake game where we create the snake board
"""

import sys
import svg

def generate_background(width, height):
    """Generate a svg image with the background"""
    print(svg.generate_start_tag_image(width, height))
    print(svg.generate_color_zone(0, 0, width, height, "grey"))
    print(svg.generate_end_tag_image())


def main():
    """Main function"""

    if len(sys.argv) != 3:
        print("Usage of the program: ./ snake_game.py width height > result.svg")
        sys.exit(1)

    width, height = int(sys.argv[1]), int(sys.argv[2])

    if width < 40 or height < 40:
        print("Please the height and the width need to be > 40.")
        sys.exit(1)

    generate_background(width, height)


if __name__ == "__main__":
    main()
