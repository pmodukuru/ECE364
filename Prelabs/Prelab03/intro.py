#! /bin/evn python3.5

def getHeadAverage(l, n):
    return sum(l[:n]) / len(l[:n])

def getTailMax(l, m):
    return max(l[-m:])

def getNumberAverage(l):
    numlist = []

    for i in l:
        if type(i) is int or type(i) is float:
            numlist.append(i)
    return sum(numlist)/len(numlist)

def getFormattedSSN(n):
    SSN = str(n)

    if len(SSN) > 9 or n < 0:
        return "SSN is not in correct form"

    while len(SSN) < 9:
        SSN = '0' + SSN

    return SSN[:3] + "-" + SSN[3:5] + "-" + SSN[5:]

def findName(l, s):
    for fullnm in l:
        strnm = fullnm.split()
        if strnm[0] == s or strnm[1] == s:
           return ' '.join(strnm)
    return "Not found in list"

def getColumnSum(mat):
    sumlist = []
    for col in mat:
        sumlist.append(sum(col))

    return sumlist

def getFormattedNames(ln):
    namelist = []
    for name in ln:
        first = name[0]
        mid = name[1]
        last = name[2]

        mid = mid + '.'
        last = last + ','
        nwname = [last, first, mid]
        namelist.append(" ".join(nwname))

    return namelist

def getElementwiseSum(l1, l2):
    #if list1 is smaller than list 2
    if len(l1) < len(l2):
        for i in range(len(l2)-len(l1)):
            l1.append(0)
    #if list2 is smaller than list 1
    if len(l2) < len(l1):
        for i in range(len(l1)-len(l2)):
            l2.append(0)
    return [a + b for a, b in zip(l1, l2)]

def removeDuplicates(l):
    #init
    list = []

    for i in l:
        if not i in list:
            list.append(i)

    return list

def getMaxOccurrence(l):
    maxcnt = 0

    for i in l:
        if l.count(i) > maxcnt:
            maxcnt = l.count(i)
            maxnum = i
    return maxnum

def getMaxProduct(l):
    maxprod = 0
    for i in range(len(l) - 2):
        prod = l[i] * l[i+1] * l[i+2]
        if prod > maxprod:
            maxprod = prod
    return maxprod

if __name__ == "__main__":

    #testing getHeadAverage
    print("\nTesting getHeadAverage")
    l = [1, 2, 3, 4, 8]
    n = 3
    print("1st {} items of List: {}".format(n,l))
    print("Average: {}".format(getHeadAverage(l,n)))

    # testing getTailMax
    print("\nTesting getTailMax")
    l = [1, 2, 9, 4, -1, -3]
    m = 2
    print("Last {} items of List: {}".format(m, l))
    print("Max: {}".format(getTailMax(l, m)))

    # testing getNumberAverage
    print("\nTesting getNumberAverage")
    l = [1, 2, "Blue", 4, 1, True, "Hello", 9, 3, 3.4]
    print("Items of List: {}".format(l))
    print("Avg: {}".format(getNumberAverage(l)))

    #testing getFormattedSSN
    print("\nTesting getFormattedSSN")
    s = 1657649
    print("num: {}".format(s))
    print("SSN {}:".format(getFormattedSSN(s)))

    #testing findName
    print("\nTesting findName")
    l = ["George Smith", "Mark Johnson", "Cordell Theodore", "Maria Satterfield", "Johnson Cadence"]
    s = "Johnson"
    print("Name: {}".format(s))
    print(findName(l,s))

    #testing getColumnSum
    print("\nTesting getColumnSum")
    l1 = [2, 3, 4]
    l2 = [4, -4, 3]
    l3 = [5, 0, -12]
    mat = [l1, l2, l3]
    print(getColumnSum(mat))

    #testing getFormattedNames
    print("\nTesting getFormattedNames")
    l1 = ["George", "W", "Bush"]
    l2 = ["Prady", "H", "Modukuru"]
    l3 = ["Albert", "A", "Einstein"]
    list = [l1, l2 , l3]
    print(getFormattedNames(list))

    #testing getElementwiseSum
    print("\nTesting getElementwiseSum")
    l1 = [1, 3, 5, 7, 9, 11]
    l2 = [6, 4, 2]
    print(getElementwiseSum(l2, l1))

    #testing removeDuplicates
    print("\nTesting removeDuplicates")
    l1 = [1, 1, 3, 2, 2, 7, 9, 2, 2, 11, 2]
    print(removeDuplicates(l1))

    #testing getMaxOccurrence
    print("\nTesting getMaxOccurrence")
    l1 = [1 ,2 ,3 ,4 , 3, 2, 4, 5, 2]
    print(getMaxOccurrence(l1))

    #testing getMaxProduct
    l3 = [3, 7, -2, 2, 3, 5]
    print(getMaxProduct(l3)) # p = 30