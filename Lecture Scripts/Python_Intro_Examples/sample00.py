#!/usr/local/bin/python3.4
"""
Script samples for ECE 364.
"""

import os
import sys

# print("Loose statements Part I ...")

def FirstMethodInTheFile():
    """
    Sample method comments.
    """
    x = 1
    print(x)
    print("First Method.")

    # Calling the second method below.
    SecondMethodInTheFile()

def SecondMethodInTheFile():
    """
    Another method help content.
    """
    print("Second Method.")

# print("Loose statements Part II ...")


# Entry-point
if __name__ == "__main__":
    print("Beginning the Main method.")
    FirstMethodInTheFile()
