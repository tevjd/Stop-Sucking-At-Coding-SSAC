#!/usr/bin/env python3
"""This is a test module with two basics functions"""

def ask_int():
    """Ask a int and return it"""
    integer_asked = int(input("Give an integer please:\n"))
    return integer_asked

def ask_string():
    """Ask a string and return it"""
    string_asked = input("Give a string please:\n")
    return string_asked

print("__name__ =", __name__)

def test_integer():
    """Test the integer function"""
    int1 = ask_int()
    int2 = ask_int()
    print("This is the sum: ", int1+int2)

if __name__ == "__main__":
    test_integer()
