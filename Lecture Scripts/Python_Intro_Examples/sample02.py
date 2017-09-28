#!/usr/bin/env python3.4

"""
Script samples for ECE 364.
"""

__version__ = '1.0.0'
__author__ = "Alex Gheith"
__date__ = '2014-February-03'

import os
import math

def workWithLists():
    """
    Line one.
    line two.
    """

    list1 = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    list2 = list1

    print("Length of the List is: ".format(len(list1)))
    print(list1[1])
    print(list1[0:])
    print(list1[:5])
    print(list1 [1:6]) # first .... (Last-1)
    i = 1
    print(list1[i:i+5])
    print()
    print("List: {}".format(list1))
    rlist = list1.reverse()

    print("Reversed: {}".format(list1))
    print("Reversed2: {}".format(rlist))
    print("List2: {}".format(list2))

    list1.reverse()
    list1.append(121)

    print()
    print("After appending: ".format(list1))

    # Another way to print: print("Negative indices: %d, %d" % (list[-1], list[-5])) # <= Note: Take a tuple.
    print("Negative indices: {}, {}".format(list1[-1], list1[-5]))


def workWithLoops():

    vector = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    # Get the vector norm, which is the square-root of the sum of the elements squared.
    vectorNorm = 0

    for element in vector:
        vectorNorm += element ** 2.0

    vectorNorm = math.sqrt(vectorNorm)

    normalizedVector = []

    for element in vector:
        normalizedVector.append(element / vectorNorm)

    print()
    print("Looping Example 1")
    print("Vector: \t{0}\n\nVector Norm = {1} or approx. {1:3.1f}\n\nNormalized Vector:\t {2}\n\n".format(vector, vectorNorm, normalizedVector))


def workWithLoopsUsingRange():
    """
    This example is a VERY BAD LOOPING MECHANISM. It is presented only for explanation.
    """
    vector = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    elementCount = len(vector)

    # Get the vector norm, which is the square-root of the sum of the elements squared.
    vectorNorm = 0

    for index in range(elementCount):
        element = vector[index]
        vectorNorm += element ** 2.0

    vectorNorm = math.sqrt(vectorNorm)

    normalizedVector = []

    for index in range(elementCount):
        element = vector[index]
        rounded = round(element / vectorNorm, 3)
        normalizedVector.append(rounded)

    print()
    print("Looping Example 2")
    print("Vector: \t{0}\n\nVector Norm = {1} or approx. {1:3.1f}\n\nNormalized Vector:\t {2}\n\n".format(vector, vectorNorm, normalizedVector))

if __name__ == "__main__":
    workWithLists()
    workWithLoops()
    workWithLoopsUsingRange()
