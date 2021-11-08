# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
__author__ = "Keshavaditya Golla"
__email__ = "keshav.aditya19@gmail.com"


import numpy as np


def get_average(student):
    homework = np.average(student['homework'])
    quizzes = np.average(student['quizzes'])
    tests = np.average(student['tests'])
    get_average = (0.1 * homework) + (0.3 * quizzes) + (0.6 * tests)
    return get_average


def get_letter_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


def get_class_average(class_list):
    results = []
    for student in class_list:
        b = get_average(student)
        results.append(b)
    return np.average(results)


if __name__ == "__main__":

    lloyd = {
        "name":     "Lloyd",
        "homework": [90.0, 97.0, 75.0, 92.0],
        "quizzes":  [88.0, 40.0, 94.0],
        "tests":    [75.0, 90.0]
    }
    alice = {
        "name":     "Alice",
        "homework": [100.0, 92.0, 98.0, 100.0],
        "quizzes":  [82.0, 83.0, 91.0],
        "tests":    [89.0, 97.0]
    }
    tyler = {
        "name":     "Tyler",
        "homework": [0.0, 87.0, 75.0, 22.0],
        "quizzes":  [0.0, 75.0, 78.0],
        "tests":    [100.0, 100.0]
    }

    students = [lloyd, alice, tyler]
    print(get_class_average(students))
