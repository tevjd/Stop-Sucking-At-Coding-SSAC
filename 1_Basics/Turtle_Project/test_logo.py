#!/usr/bin/env python3

"""Test file for the logo module."""

import logo
import svg


def main():
    """We draw something with the logo module."""

    print(svg.generate_start_tag_image(100, 100))
    print(
        svg.generate_start_tag_group(
            line_color="black", padding_color="none", line_thickness=3
        )
    )

    # Initial position
    abscisse = 0.0
    ordonnee = 0.0
    # Angle based on the origin so the tutle is looking up
    direction = 90.0
    # False = only moving, True = draw something
    crayon_en_bas = False

    # Just moving
    direction = logo.turn_right(direction, 180.0)
    abscisse, ordonnee = logo.forward(abscisse, ordonnee, direction, crayon_en_bas, 50.0)
    direction = logo.turn_left(direction, 90.0)
    abscisse, ordonnee = logo.forward(abscisse, ordonnee, direction, crayon_en_bas, 50.0)
    direction = logo.turn_left(direction, 90.0)

    # On va dessiner un premier truc
    crayon_en_bas = True
    abscisse, ordonnee = logo.forward(abscisse, ordonnee, direction, crayon_en_bas, 20.0)
    direction = logo.turn_right(direction, 90.0)
    abscisse, ordonnee = logo.forward(abscisse, ordonnee, direction, crayon_en_bas, 20.0)
    direction = logo.turn_right(direction, 90.0)
    abscisse, ordonnee = logo.forward(abscisse, ordonnee, direction, crayon_en_bas, 20.0)
    direction = logo.turn_right(direction, 90.0)
    abscisse, ordonnee = logo.forward(abscisse, ordonnee, direction, crayon_en_bas, 20.0)

    # On se déplace sans dessiner
    crayon_en_bas = False
    abscisse, ordonnee = logo.forward(abscisse, ordonnee, direction, crayon_en_bas, 20.0)

    # On dessine un deuxième truc
    crayon_en_bas = True
    abscisse, ordonnee = logo.forward(abscisse, ordonnee, direction, crayon_en_bas, 20.0)
    direction = logo.turn_right(direction, 90.0)
    abscisse, ordonnee = logo.forward(abscisse, ordonnee, direction, crayon_en_bas, 20.0)
    direction = logo.turn_right(direction, 90.0)
    abscisse, ordonnee = logo.forward(abscisse, ordonnee, direction, crayon_en_bas, 20.0)
    direction = logo.turn_right(direction, 90.0)
    abscisse, ordonnee = logo.forward(abscisse, ordonnee, direction, crayon_en_bas, 20.0)

    # On se déplace sans dessiner
    crayon_en_bas = False
    direction = logo.turn_right(direction, 90.0)
    abscisse, ordonnee = logo.forward(abscisse, ordonnee, direction, crayon_en_bas, 20.0)
    direction = logo.turn_left(direction, 90.0)
    abscisse, ordonnee = logo.forward(abscisse, ordonnee, direction, crayon_en_bas, 10.0)

    # On dessine un troisième truc
    crayon_en_bas = True
    direction = logo.turn_left(direction, 45.0)
    abscisse, ordonnee = logo.forward(abscisse, ordonnee, direction, crayon_en_bas, 30.0)
    direction = logo.turn_left(direction, 45.0)
    abscisse, ordonnee = logo.forward(abscisse, ordonnee, direction, crayon_en_bas, 30.0)
    direction = logo.turn_left(direction, 45.0)
    abscisse, ordonnee = logo.forward(abscisse, ordonnee, direction, crayon_en_bas, 30.0)

    # On termine l'image SVG
    print(svg.generate_end_tag_group())
    print(svg.generate_end_tag_image())


main()
