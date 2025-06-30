#!/usr/bin/env python3
"""This is a module for cryptography encoding"""

def is_single_letter(letter):
    """
    Function that determine if letter is a string of length 1 and
    uppercase or lowercase
    """
    if not isinstance(letter, str):
        raise ValueError("Input must be a string.")
    if len(letter) != 1:
        raise ValueError("Input must be length of 1.")
    if not letter.isalpha():
        raise ValueError("Input must be a letter.")
    return True

def rot(letter, shift):
    """This function take a letter and return the letter shifted in the alphabet"""
    if is_single_letter(letter):
        if letter.isupper():
            shifted = chr(((ord(letter) - ord('A')) + shift)%26 + ord('A'))
        else:
            shifted = chr(((ord(letter) - ord('a')) + shift)%26 + ord('a'))
        return shifted

def rot13(letter):
    """Same as before but here we have a shift of 13"""
    return rot(letter, 13)
