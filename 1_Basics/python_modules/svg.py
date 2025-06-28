#!/usr/bin/env python3

"""
This is a module to generate SVG images.
We can see there is different functions in this module to generate elements of
an SVG image. 
"""

def generate_start_tag_image(width, height):
    """
    Return the string for opening the SVG image. 
    We also have to specify the size of the image = width and height

    Note that the origin is in the left up corner and goes down. 
    """
    return f"<svg xmlns='http://www.w3.org/2000/svg' version='1.1'" \
         f" width='{width}' height='{height}'>\n"


def generate_end_tag_image():
    """
    Return the closing tag for the image
    """
    return "</svg>\n"


def generate_start_tag_group(line_color, padding_color, line_thickness):
    """
    Return starting tag for a group. The color parameters can be a color like "red" 
    or "none" that is mean there is no padding. 
    """
    return f"<g stroke='{line_color}' stroke-width='{line_thickness}' fill='{padding_color}'>\n"


def generate_end_tag_group():
    """
    Return end tag for a group.
    """
    return "</g>\n"


def generate_circle(circle, radius):
    """
    Return tag for drawing a circle in SVG. Center is a tuple and radius an integer.
    """
    return f"<circle cx='{circle[0]}' cy='{circle[1]}' r='{radius}'/>\n"


def generate_line(start, end, color, width):
    """
    Return the svg tag to draw a line. This line is a link between the start and end point. 
    A point is a tuple with two integer. 
    """
    return f"<line x1='{start[0]}' y1='{start[1]}' x2='{end[0]}' y2='{end[1]}' " \
         f" style='stroke:{color};stroke-width:{width}' />"


# À implémenter dans `TP Optionnels Échiquier`
def genere_rectangle(top_left, width, height):
    """
    Retourne la chaîne de caractères correspondant à un élément SVG représentant un rectangle.
    """
    # TODO
    ...


# À implémenter dans `TP7. Kaléidoscope`
def genere_polygone(points):
    """
    Retourne la chaîne de caractères correspondant à un élément SVG
    représentant un polygone. `points` est un tableau de points qui
    sont eux mêmes des tuples de deux nombres.
    """
    # TODO
    ...


# À implémenter dans `TP7. Kaléidoscope`
def genere_balise_debut_groupe_transp(niveau_opacite):
    """
    Retourne la chaîne de caractères correspondant à une balise ouvrant un
    groupe d'éléments qui, dans son ensemble, sera partiellement transparent.
    Les éléments qui composent le groupe se masquent les uns les autres dans
    l'ordre d'apparition (ils ne sont pas transparents entre eux).
    `niveau_opacite` doit être un nombre entre 0 et 1. Ce groupe doit être
    refermé de la même manière que les groupes définissant un style.
    """
    # TODO
    ...


# À implémenter dans `TP8. Plateau`
def genere_zone_colorie(x_min, y_min, width, height, padding_color):
    """
    Retourne la chaîne de caractères correspondant à un élément qui colorie une
    zone rectangulaire de la couleur indiquée
    """
    # TODO
    ...


# À implémenter dans `TP8. Plateau`
def genere_texte(x_min, y_bas, contenu, height):
    """
    Retourne la chaîne de caractères correspondant à un élément SVG représentant
    un texte. Place le texte à la position indiquée. x_min est l'abscisse du
    début du texte. y_bas est l'ordonnée de la ligne de base du texte (le bas
    d'une lettre telle que “n”). Attention, ce n'est pas l'ordonnée maximale
    puisque certaines lettres descendent sous cette ligne (g, j, p, q, y). Le
    paramètre height définit la taille de police (c'est-à-dire la height d'une
    ligne de texte)
    """
    # TODO
    ...
