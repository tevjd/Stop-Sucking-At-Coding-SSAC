#!/usr/bin/env python3

"""Test for my first module"""

import first_module

def main():
    """Test the functions of the first module"""
    #start by asking a number
    integer_test = first_module.ask_int()
    if not isinstance(integer_test, int):
        print("The integer the user gave us is not an integer.")

    string_test = first_module.ask_string()
    if not isinstance(string_test, str):
        print("The string the user gave us is not a string.")

    print(f"This is the result, integer = {integer_test} and the string = {string_test}.")

if __name__ == "__main__":
    main()
