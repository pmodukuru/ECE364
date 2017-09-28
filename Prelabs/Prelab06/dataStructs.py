import os
import glob
import sys


def uniqueLetters(s):
    unique = set(s)
    unique = list(unique)
    unique.sort(reverse=True)

    return "".join(unique)

def scaleSet(aSet, num):
    nset = set()
    for e in aSet:
        nset.add(round(e * num, 2))
    return nset

def printNames(aSet):
    l = list(aSet)
    l.sort()
    for name in l:
        print(name)

def getStateName(nm):
    dict = {"Indiana": "IN", "California": "CA", "Ohio": "OH", "Alabama": "AL", "New York": "NY"}

    for key, value in dict.items():
        if nm == value:
            return key
    return None

def getZipCodes(statenm):
    d1 = {"Indiana": "IN", "California": "CA", "Ohio": "OH", "Alabama": "AL", "New York": "NY"}
    d2 = {47906: "IN", 47907: "IN", 10001: "NY", 10025: "NY", 90001: "CA", 90005: "CA", 90009: "CA"}
    zipset = set()

    state = None
    for name, abb in d1.items():
        if name == statenm:
            state = abb
    for zip, abb in d2.items():
        if abb == state:
            zipset.add(zip)

    return zipset

def printSortedMap(s):

    slist = []
    for (lastName, firstName, mi), weight in s.items():
        o = "{1} {2} {0} has a weight of {3} lb.".format(lastName, firstName, mi, weight)
        slist.append(o)
    slist.sort()

    for i in slist:
        print(i)

def switchNames(s):
    nws = dict()
    keylist = []

    for key, val in s.items():
        keylist = [key[1], key[0]]
        nws[" ".join(keylist)] = val

    return nws

def getPossibleMatches(record, n):
    names = set()

    for key, (MM, DD, YY) in record.items():
        if MM == n or DD == n or YY == n:
            names.add(key)
    return names

def getPurchaseReport():
    inventory = {}
    itemlist = "purchases/Item List.txt"
    itemdict = {}
    tranlist = []
    finaldict = {}
    ID = 0;
    with open(itemlist, 'r') as myFile:
        all_lines = myFile.readlines()

    #create item dictionary
    for line in all_lines[2:]:
        tline = line.split()
        str = tline[1]
        itemdict[tline[0]] = str[1:]

    #read through all transaction files
    trans = glob.glob("purchases/purchase_*.txt")
    for order in trans:
        tranlist = []
        cost = 0
        with open(order, 'r') as tfile:
            all_lines = tfile.readlines()
        for line in all_lines[2:]:
            tline = line.split()
            tline = tuple(tline)
            tranlist.append(tline)
        for item, num in tranlist:
            str = itemdict[item]
            print("Price {} * num {} = {}".format(str[:], num, float(str[:]) * float(num)))
            cost += float(str[:]) * float(num)
            print(cost)
        finaldict[ID] = round(cost, 2)
        ID += 1
        cost += 1

    print(finaldict)







if __name__ == "__main__":

    print(uniqueLetters("ABDBDARWET"))

    aSet = {3.12, 5.0, 7.2, 15.24}
    print(scaleSet(aSet, 2.1))

    aSet = {"Prady", "Priya", "Pushkal", "Manav", "Neel", "Justin", "Alfred"}
    printNames(aSet)

    print(getStateName("IN"))

    print(getZipCodes("California"))

    s = {("Frank", "Xavier", "L"): 209.9, ("James", "Rodney", "M"): 199.0, ("George", "Johnson", "T"): 250.9}
    printSortedMap(s)

    s = {("Frank", "Xavier", "L"): 209.9, ("James", "Rodney", "M"): 199.0, ("George", "Johnson", "T"): 250.9}
    news = switchNames(s)
    print(news.items())

    record = {"Prady": (8, 12, 96), "Hello": (12, 23, 85), "hi": (8, 12, 96)}
    print(getPossibleMatches(record, 12))

    getPurchaseReport()