#!/usr/local/bin/python3.4

"""
Script samples for ECE 364: THIS IS OK.
"""
import sys

def addTwoNumbers(a, b):
    return a + b

if __name__ == "__main__":

    if len(sys.argv) == 2:
        inputFileName = sys.argv[1]
    else:
        inputFileName = "somefile.txt"

    # Work with your input file ...

    x1 = 3
    x2 = 10

    total = addTwoNumbers(x1, x2)

    print("The sum of {0} and {1} is {2}".format(x1, x2, total))
