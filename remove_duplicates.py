# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
__author__ = "Keshavaditya Golla"
__email__ = "keshav.aditya19@gmail.com"


def remove_duplicates(input_list):
    if not input_list:
        return "Empty input list"

    input_list = sorted(input_list)     # Sort the input list from low to high
    output_list = [input_list[0]]       # Initialize the output list and assign the first value of the sorted input list

    # Go through the values of the sorted list and append to the output list
    # any values that are greater than the last value of the output list
    for i in input_list:
        if i > output_list[-1]:
            output_list.append(i)

    return output_list


if __name__ == "__main__":

    print(remove_duplicates([1, 1, 2, 2, 1, 2, 3, 4, 5, 6, 7, 8, 5, 4, 3, 2, 1, 1]))
