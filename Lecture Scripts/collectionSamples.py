#! /usr/local/bin/python3.4

"""
An example file for the collections' lecture.
"""

# Check how the "in" operator works for all the collections.

##############################
#### Lists
##############################

# Type test.
x = [0, 9, 4, 3, 1]
y = type(x) is list; print("Is 'x' a list? => {0}".format(y)) # Preferred!
z = type(x) == list; print("Does 'x' equal a list? => {0}".format(y))

print("Type of x is {}".format(type(x)))

# Membership check.
x = ['Mike', 'Rodney', 'Joan', 'Susan']
y = 'susan'
print(y in x)

# Adding an element at the end of the list.
x = [0, 9, 4, 3, 1]
x.append(2); print(x)
# x.extend(4)   # Wrong!!!

# Extending the list.
x = [0, 9, 4, 3, 1]
y = [10, 20]
x.extend(y); print(x)
# CAREFUL: x is correct, but produces a different result.

# Concatenating (Extending).
x = [0, 9, 4, 3, 1]
y = [10, 20]
z = x + y; print(z)

# Some list functions.
x = [0, 9, 4, 3, 1, 3, 2, 0, 9, 10]
print(x.index(9))

x = [0, 9, 4, 3, 1, 3, 2, 0]
print(x.count(0))

x = [0, 1, 2, 3, 4, 5]; print(x)
x.reverse(); print(x) # Changes the list in place.

x = [4, 6, 0, 1, 2, 3]; print(x)
x.sort(); print(x) # Changes the list in place.

print()
x = [4, 6, 0, 1, 2, 3]; print(x)
x.sort(reverse=True); print(x)

# sorted(), reversed().
# These do NOT change the list in place.
print()
x = [4, 6, 0, 1, 2, 3]; print("x = {0}".format(x))
y = sorted(x, reverse=True); print("y = {0}".format(y))
z = reversed(x); print("z = {0}".format(z))
w = list(z); print("w = {0}".format(w))
print("x = {0}".format(x))

##########################
#### Tuples
##############################

# Note that the parentheses are optional.
t = (1.4, 2.3)
print("Type of t is {}".format(type(t)))
f = type(t) is tuple
print("Is 't' a tuple? {0}".format(f))

x = 3
y = 4
t = x, y    # Packing.
print("Type of t is {}".format(type(t)))

# Unpacking.
t = (3.14, "Alex", [5, 4]) # NOTE: List are "referenced".
x, y, z = t     # TRY: x, y, z, s, q = t
print("x = {}, y = {}, z = {}".format(x, y, z))

# Use of the placeholder.
t = (1.4, 2.3, 12)
x, _, w = t
print("x = {}".format(x))

# Unpack in a loop.
t2 = [("A", 1), ("B", 2), ("C", 3)]

for letter, order in t2:
    print("Letter {0} is No. {1}.".format(letter, order))

# Works with lists too! But slower for larger codebase.
l2 = [["A", 1], ["B", 2], ["C", 3]]

for letter, order in l2:
    print("The letter {0} is No. {1} in the Alphabet.".format(letter, order))

# Named Tuple:
from collections import namedtuple
Student = namedtuple("Student", ["First", "Last", "ID"])
s1 = Student(First="Mary", Last="Smith", ID=1234567890)
s2 = Student("John", "Travolta", ID=12345678)

##############################
#### Sets
##############################
l = list("Apple")
s = set(l)
print('The list is: {}'.format(l))
print('The set is: {}'.format(s))

s1 = set("app")
s2 = set("pete")
print("s1 = {} and s2 = {}".format(s1, s2))

setDiff = s1 - s2   # OR s1.difference(s2)
setUnion = s1 | s2  # OR s1.union(s2)
s3 = s2.copy()
setIntersection = s3 & s2   # OR s1.intersection(s2, s3)

print("Diff = {}.".format(setDiff))
print("Union = {}".format(setUnion))
print("Intersection = {}".format(setIntersection))

##############################
#### Dictionaries (Maps)
##############################

# => What can be a key?
# int, float, string, tuple BUT NOT LIST, SET nor DICTIONARY.

# => What can be a value?
# Everything.


# Each dictionary entry is a item that has a key and a value.
myMap = {121: "John the 3rd",
         295: "Todd Son of Aragorn",
         330: "Christine of England",
         559: "Queen Mary of Someplace",
         670: "Elisabeth Trudy Jr."}

from pprint import pprint as pp
print(myMap)
pp(myMap)

print("Keys are {}".format(myMap.keys()))
print("Values are {}".format(myMap.values()))
print("Items are {}".format(myMap.items()))

for k in myMap.keys():
    print(k)

for v in myMap.values():
    print(v)

for k, v in myMap.items():
    print("For key {}, the Value is {}".format(k, v))

for i in myMap:
    print("The value of the iterator is {}".format(i))

print(myMap[121])

print(myMap["000"])

k = 121
answer = "is" if k in myMap else "is NOT"
print("The key {0} {1} in myMap!".format(k, answer))


##############################
#### File I/O
##############################
fileName = 'names.txt'

# with open(fileName, 'r') as f:
#
#     for line in f:
#         print(line)

with open(fileName, 'r') as f:
    content1 = f.readline()
    content2 = f.readline()

print(content1)
print(content2)

with open(fileName, 'r') as f:
    contentAll = f.readlines()

# We are now outside the scope of the with-block. Resources released.
print(contentAll)
