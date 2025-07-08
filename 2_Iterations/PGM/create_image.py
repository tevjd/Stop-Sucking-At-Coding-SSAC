#!/usr/bin/env python3
"""This is a file that creat PGM image"""

from random import randint

def main():
    """This is the main function"""

    height = int(input("Give the heigth of the image: \n"))
    wide = int(input("Give the wide of the image: \n"))

    min_radius = min(height*0.2, wide*0.2)

    center1_x, center1_y = randint(min_radius, wide-min_radius), \
        randint(min_radius, height-min_radius)
    max_radius1 = min(center1_x, wide-center1_x, center1_y, height-center1_y)
    radius1 = randint(min_radius, max_radius1)

    center2_x, center2_y = randint(min_radius, wide-min_radius), \
        randint(min_radius, height-min_radius)
    max_radius2 = min(center2_x, wide-center2_x, center2_y, height-center2_y)
    radius2 = randint(min_radius, max_radius2)

    f = open("test.pgm", 'w', encoding='utf-8')
    print(f"P2\n{wide} {height}\n255", file=f)
    for y in range(0, height):
        for x in range(0, wide):
            if (((x - center1_x)**2 + (y - center1_y)**2 <= radius1**2) or
                ((x - center2_x)**2 + (y - center2_y)**2 <= radius2**2)):
                print(randint(0, 255), end=" ", file=f)
            else:
                print("255", end=" ", file=f)
        print("", file=f)
    f.close()


if __name__ == "__main__":
    main()
