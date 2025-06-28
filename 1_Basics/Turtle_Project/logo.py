#!/usr/bin/env python3

"""
Turtle logo module.
We will find some graphical functions for turtle logo.
"""
import math
import svg



def forward(abscisse, ordonnee, direction, pen_down, distance):
    """
    The turtle goes forward.
    We draw a line in the direction and the distance in parameters (if the pen is down). 
    We return the new position as a tuple of 2 floats.
    Note that the component are respresented with (0, 0) as origin in the top left corner. 
    """
    #first we compute the end point
    angle_radian = math.radians(direction)
    delta_x, delta_y = distance*math.cos(angle_radian), distance*math.sin(angle_radian)
    end_x, end_y = abscisse + delta_x, ordonnee - delta_y

    if pen_down:
        print(svg.generate_line((abscisse, ordonnee), (end_x, end_y), "black", 2))

    return (end_x, end_y)


def turn_right(direction, angle):
    """
    Tutle goes on right. 
    Return the new direction. 
    """
    return (direction - angle)%360


def turn_left(direction, angle):
    """
    Same as before but for the left
    """
    return (direction + angle)%360
