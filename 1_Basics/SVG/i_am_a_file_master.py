#!/usr/bin/env python3
"""Test file to manipulate other files"""


def main():
    """Open a file and write in it"""
    myfile = open("toto.txt", "w", encoding="utf-8")
    myfile.write("This is the first line of my document here.\n")
    print("This is the second line here.", file=myfile)
    myfile.close()

if __name__ == "__main__":
    main()
