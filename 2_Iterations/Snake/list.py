#!/usr/bin/env python3
""""
This program is an introduction to python list.
We can't use append, insert, remove or del
"""


from random import randint

def create(size):
    """Create a list of length size with random [1, 9] numbers"""
    tab = [randint(0, 9) for _ in range(size)]
    return tab

def index_first_occurency(tab, target):
    """Return the index of the first occurency in tab or -1 of none"""
    for i, elem in enumerate(tab):
        if elem == target:
            return i
    return -1

def exchange(tab, idx1, idx2):
    """Exchange idx1 and idx2 in tab"""
    tamp = tab[idx1]
    tab[idx1] = tab[idx2]
    tab[idx2] = tamp
    return tab

def invert(tab):
    """Invert tab with the exchnage function"""
    first = 0
    last = len(tab)-1
    while first < last:
        tab = exchange(tab, first, last)
        first += 1
        last -= 1
    return tab

def min_and_max(tab):
    """Get the min and max of the tab"""
    mini = 10
    idx_min = -1
    maxi = 0
    idx_max = -1
    for i, elem in enumerate(tab):
        if elem < mini:
            idx_min = i
            mini = elem
        if elem > maxi:
            idx_max = i
            maxi = elem
    return (idx_min, idx_max)


def main():
    """Main function of the program"""
    for size in range(6):
        print("-- Size =", size, "--")
        tab = create(size)
        print("Original list :", tab)
        for idx in range(size):
            print("Index of", tab[idx], ":", index_first_occurency(tab, tab[idx]))
        print("Index of 10 :", index_first_occurency(tab, 10))
        invert(tab)
        print("Reverse list :", tab)
        idx_min, idx_max = min_and_max(tab)
        if idx_min == idx_max == -1:
            print("There is no min nor max in an empty list!")
        else: 
            print(f"Min value {tab[idx_min]} at index {idx_min}")
            print(f"Max value {tab[idx_max]} at index {idx_max}")
        print()


main()
