#!/usr/bin/env python3

"""This is a test file to learn how to use tuple"""

datas = [(17, 9), (15, 6), (4, 1)]

def compute_average():
    """Compute the average grade of the student based on datas"""
    coef = 0
    sum_coef = 0
    for data in datas :
        coef += data[1]
        sum_coef += (data[0] * data[1])
    print(f"The average of this student is {sum_coef/coef}.")

if __name__ == "__main__":
    compute_average()
