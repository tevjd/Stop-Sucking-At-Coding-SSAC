#!/usr/bin/env python
"""Shebang to tell the OS which interpreter to use"""

def main():
    """Main function of the program"""
    #We ask for the age of the captain
    age_captain = int(input('Give me the age of the Captain!\n'))
    current_year = 2025
    new_age = age_captain + (2050 - current_year)
    print(f"This is the new age of the Captain: {new_age}")

if __name__ == "__main__":
    #print('This is my first script as a test.')
    main()
