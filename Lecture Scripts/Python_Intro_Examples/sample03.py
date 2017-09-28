#!/usr/bin/env python3.4
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
# multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

"""
Script samples for ECE 364.
"""

__version__ = '1.0.0'
__author__ = "Alex Gheith"
__date__ = '2014-February-03'

import os

def solveByMethodOne(maxValue):

    value = 0
    totalSum = 0

    while value < maxValue :
        if not (value % 3) or not (value % 5) :
            totalSum += value
        value += 1

    return totalSum

def solveByMethodTwo(maxValue):

    totalSum = 0

    for value in range(1000):

        if not (value % 3) or not (value % 5):
            totalSum += value

    return totalSum

if __name__ == "__main__":
    totalSum = solveByMethodOne(1000)
    print("Solution using Method 1 = {}".format(totalSum))

    totalSum = solveByMethodTwo(1000)
    print("Solution using Method 2 = {}".format(totalSum))
