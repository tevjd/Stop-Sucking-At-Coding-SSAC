#!/usr/bin/env python3
"""This is a test file to discover the f-string"""

def main():
    """Main function to test f-strings format"""
    prenom = "Alexa"
    age = 10
    message_perso = f"Hello I am {prenom} and I am {age}."
    print(message_perso)

def convert_point_to_chain(x, y):
    """Function to convert a point in a string with coordonates"""
    print(f"Here is the coordonate of the point: {(x, y)}")

main()
convert_point_to_chain(12.2, 3.3)
