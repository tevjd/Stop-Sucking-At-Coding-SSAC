#!/usr/bin/env python3
"""This is a program that detects peak in a list"""

def extremum(prec, curr, suiv):
    """This function check that curr is an extremum or not"""

    if prec < curr > suiv:
        print(f"Extremum detected (local max): {curr}")
        return True
    if prec > curr < suiv:
        print(f"Extremum detected (local min): {curr}")
        return True
    return False


def check_different_number(value):
    """Function that read integer and return if the number is different or negative"""

    while True:
        checker = int(input())
        if checker < 0:
            return None
        elif value != checker:
            return checker

def detect_peak():
    """This function detect the peaks in a sequence of positive number"""

    print("Enter positive number (put a negative number to stop): ")

    first_interger = int(input())

    if first_interger < 0:
        print("Number of extremum: 0")
        return

    second_integer = check_different_number(first_interger)
    if second_integer is None:
        print("Number of extremum: 1")
        return

    prec = first_interger
    curr = second_integer
    number_of_extremum = 2

    while True:
        suiv = check_different_number(curr)
        if suiv is None:
            break
        if extremum(prec, curr, suiv):
            number_of_extremum += 1

        prec = curr
        curr = suiv

    print(f"Number of extremum {number_of_extremum}")

if __name__ == "__main__":
    detect_peak()