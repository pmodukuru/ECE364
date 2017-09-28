def uniqueLetters(s):
    ls = list(s)
    ss = set(ls)
    ls = list(ss)
    ls.sort(reverse=True)
    string = ''.join(ls)
    return string

def uniqueLetters_oneline(s):
    ls = list(set(list(s)))
    ls.sort(reverse=True)
    return ''.join(ls)

def scaleSet(aSet, num):
    return {round(val*num,2) for val in aSet}

def printNames(aSet):
    alist = list(aSet)
    alist.sort()

    [print(val) for val in alist]

def getStateName(stateAbb):
    nmabb = {"Indiana": "IN", "California": "CA", "Ohio": "OH", "Alabama": "AL", "New York": "NY"}
    abbnm = {value: key for key, value in nmabb.items()}
    return abbnm[stateAbb]

def getZipCodes(stateName):
    d1 = {"Indiana": "IN", "California": "CA", "Ohio": "OH", "Alabama": "AL", "New York": "NY"}
    d2 = {47906: "IN", 47907: "IN", 10001: "NY", 10025: "NY", 90001: "CA", 90005: "CA", 90009: "CA"}

    return {zip for zip, abb in d2.items() if abb == d1[stateName]}

def printSortedMap(s):
    slist = []
    for (lastName, firstName, mi), weight in s.items():
        o = "{1} {2} {0} has a weight of {3} lb.".format(lastName, firstName, mi, weight)
        slist.append(o)
    slist.sort()
    [print(line) for line in slist]

def switchNames(s):
    return {First+' '+Last: weight for (Last, First, mi), weight in s.items()}

def getPossibleMatches(record, n):
    return {name for name, (mm, dd, yy) in record.items() if dd == n or mm == n or yy == n}


import glob

def openFile(filename):
    with open(filename, 'r') as File:
        lines = File.readlines()
    return lines

def getPurchaseReport():
    filepath = "./purchases/Item List.txt"
    filelines = openFile(filepath)

    #create item: price dict
    tlist = [line.split() for line in filelines[2:]]
    ipdict = {item: float(price[1:]) for item, price in tlist}

    #analyze all purchases
    allfiles = glob.glob("./purchases/p*.txt")
    allfiles.sort()

    purdict = {}
    for file in allfiles:
        purdict[int(file[-7:-4])] = 0
        filelines = openFile(file)
        tlist = [line.split() for line in filelines[2:]]
        for purchase in tlist:
            purdict[int(file[-7:-4])] = round(float(purchase[1]) * ipdict[purchase[0]] + purdict[int(file[-7:-4])], 2)

if __name__ == "__main__":

    #Test 1
    print(uniqueLetters("ABDBDARWET"))
    print(uniqueLetters_oneline("ABDBDARWET"))

    #Test 2
    s = {3.12, 5.0, 7.2, 15.24}
    print(scaleSet(s, 2.1))

    #Test 3
    s = {'prady', 'alfred', 'zebra', 'clint'}
    printNames(s)

    #Test 4
    print(getStateName("NY"))

    #Test 5
    print(getZipCodes("New York"))

    #Test 6
    s = {("Frank", "Xavier", "L"): 209.9, ("James", "Rodney", "M"): 199.0, ("George", "Johnson", "T"): 250.9}
    printSortedMap(s)

    #Test 7
    s = {("Frank", "Xavier", "L"): 209.9, ("James", "Rodney", "M"): 199.0, ("George", "Johnson", "T"): 250.9}
    print(switchNames(s))

    #Test 8
    s = {"Prady Modukuru": (8,12,96), "Priya Raju": (6,26,96), "Hello world": (2,23,11)}
    print(getPossibleMatches(s, 96))

    #Test 9
    getPurchaseReport()


