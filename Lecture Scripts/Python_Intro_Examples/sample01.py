#!/usr/bin/env python3.4

"""
Script samples for ECE 364.
"""

__version__ = '1.0.0'
__author__ = "Alex Gheith"
__date__ = '2014-February-03'

import os
import math

def printVariableWithType(var):
    """
    Printing.
    """
    # Another way for printing: print("Variable is of type", type(var), " and its value is: ", var)
    print("Variable is of type {} and its value is: {} ".format(type(var), var))

def printSomePrimitiveTypes():
    """
    Examples of integral types.
    """
    s = 'This is a string. "WSS" '

    x = "This is a " + ' concatenated ' + "string"

    x = 1
    printVariableWithType(x)

    y = int(2**80)
    printVariableWithType(y)

    w = math.pi
    printVariableWithType(w)

    z = 1j
    printVariableWithType(z)

    s = "This is some string to display"
    printVariableWithType(s)

    c = "Combining a string " + "with" + " another string."
    printVariableWithType(c)


if __name__ == "__main__":
    printSomePrimitiveTypes()
