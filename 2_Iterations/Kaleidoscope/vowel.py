#!/usr/bin/env python3
"""This is a program that count the number of vowel"""

NBR = 5

def vowel_count():
    """This is a program that count the number of vowel"""

    print("Get the sequence you want to analyze (press enter between each char):")
    counter = 0
    vowel = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']

    while counter < NBR:
        sequence = input("> ")
        if sequence in vowel:
            counter += 1
            print(f"Vowel : '{sequence}' ({counter}/{NBR})")


if __name__ == "__main__":
    vowel_count()
