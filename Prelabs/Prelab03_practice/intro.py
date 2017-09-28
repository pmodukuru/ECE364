from itertools import zip_longest

def getHeadAverage(alist, n):
    return sum(alist[:n]) / len(alist[:n])

def getTailMax(alist, n):
    return max(alist[-n:])

def getNumberAverage(alist):
    avg = [i for i in alist if type(i) is int or type(i) is float]
    return getHeadAverage(avg, len(avg))

def getFormattedSSN(n):
    SSN = '{:09d}'.format(n) #formats int into string 9 chars wide and fills in zeros
    return SSN[:3] + '-' + SSN[3:5] + '-' + SSN[5:]

def findName(alist, n):
    for name in alist:
        flname = name.split()
        if flname[0] == n or flname[1] == n:
            return name
    return None

def findName_inline(alist, n):
    #doesnt work if name is not found in list
    return [name for name in alist if name.split()[0] == n or name.split()[1] == n][0]

def getColumnSum(mat):
    return [sum(col) for col in zip(*mat)]

def getFormattedNames(ln):
    return [last + ', ' + first + ' ' + MI for first, MI, last in ln]

def getElementwiseSum(l1, l2):
    return [i + j for i,j in zip_longest(l1, l2, fillvalue = 0)]

def removeDuplicates(alist):
    duplist = []
    for i in alist:
        if i not in duplist:
            duplist.append(i)
    return duplist

def getMaxOccurrence(alist):
    maxlist = [alist.count(i) for i in alist]
    return alist[maxlist.index(max(maxlist))]

def getMaxProduct(l): #more complicated solution than just using for i in range(len(l) - 2)
    maxprod = 0
    for i, val in enumerate(l):
        if i >= len(l) - 2:
            break
        prod = val * l[i+1] * l[i+2]
        if prod > maxprod:
            maxprod = prod
    return maxprod

if __name__ == "__main__":
    #test 1
    alist = [1, 3, 4, 0, -3, 6, 2.4, 4]
    print(getHeadAverage(alist, 4))

    #test 2
    print(getTailMax(alist, 3))

    #test 3
    alist = ["hello", 5, 2, 2.3, -2, -1, 3, 4.5, True, "hi", [2,3]]
    print(getNumberAverage(alist))

    #test 4
    print(getFormattedSSN(1657649))

    #test 5
    l = ["Geoge Smith", "Mark Johnson", "Cordell Theodore", "Maria Satterfield", "Johnson Cadence"]
    s = "Johnson"
    print(findName(l, s))  # n = "Mark Johnson"

    print(findName_inline(l,s))

    #test 6
    mat = [[1,2,3], [4,-3,2], [-1,3,7], [-3, 1, 5]]
    print(getColumnSum(mat))

    #test 7
    ln = [["George", "W", "Bush"], ["Prady", "H", "Modukuru"]]
    print(getFormattedNames(ln))

    #test 8
    l1 = [1, 3, 5, 7, 9, 11]
    l2 = [6, 4, 2]
    print(getElementwiseSum(l1, l2))  # l3 = [7, 7, 7, 7, 9, 11]

    #test 9
    l1 = [1, 1, 3, 2, 2, 7, 9, 2, 2, 11, 2]
    print(removeDuplicates(l1))  # u = [1, 3, 2, 7, 9, 11]

    #test 10
    l1 = [1, 1, 3, 2, 2, 7, 9, 2, 2, 11, 2]
    print(getMaxOccurrence(l1))  # m = 2

    #test 11
    l3 = [3, 7, -2, 2, 3, 5]
    print(getMaxProduct(l3))  # p = 30