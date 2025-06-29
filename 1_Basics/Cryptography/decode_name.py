#!/usr/bin/env python3
"""This is a program to test the rot module"""

import rotx

def main():
    """Main function of the program"""
    name_file = input("Please give the name of the file you want to create:\n")
    f = open(name_file, 'w', encoding="utf-8")
    for letter in name_file:
        f.write(rotx.rot13(letter))
    f.close()

if __name__ == "__main__":
    main()
