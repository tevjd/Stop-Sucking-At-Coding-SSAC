#!/usr/bin/env python3
"""This is a program to test the rot module"""

import rotx

def main():
    """Main function of the program"""
    name_file = input("Please give the name of the file you want to create:\n")
    f = open(name_file + ".txt", 'w', encoding="utf-8")
    decode = "nirPrfne"
    for letter in decode:
        f.write(rotx.rot13(letter))
    f.write('\n')
    f.close()

    print(rotx.rot('P', 4), rotx.rot('a', 4), rotx.rot('u', 4), rotx.rot('l', 4), sep='')

if __name__ == "__main__":
    main()
