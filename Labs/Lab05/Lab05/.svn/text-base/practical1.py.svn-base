from pprint import pprint as pp

def openFile(filename):
    with open(filename, 'r') as File:
        lines = File.readlines()
    return lines

def retfloat(val):
    return float(val)

def getSummary():
    lines = openFile('signals.txt')
    llist = [line.split() for line in lines]
    #print(llist[2:])
    #llist = []

    signals = llist[0][1:]
    invertlist = list(zip(*llist[2:]))
    invertlist = [list(row) for row in invertlist]
    #print(invertlist)

    rrow = []
    ilist = []
    for row in invertlist:
        rrow = []
        for val in row:
            rrow.append(float(val))
        ilist.append(rrow)
    #print(ilist[1:])

    ddict = {}
    for index, sigrow in enumerate(ilist[1:]):
        sumval = 0
        avg = 0
        minval = 0
        maxval = 0

        #print(sigrow)
        sumval = sum(sigrow)
        avg = sumval/ (len(sigrow))
        minval = min(sigrow)
        maxval = max(sigrow)

        ddict[signals[index]] = (round(minval,3), round(avg,3), round(maxval,3))

    #pp(ddict['NIK876'])


    return ddict

def saveContinuousData(start, end, targetFileName):
    lines = openFile('signals.txt')
    llist = [line.split() for line in lines]
    #print(llist[2:])
    #llist = []

    signals = llist[0][1:]

    rrow = []
    ilist = []
    for row in llist[2:]:
        rrow = []
        for val in row:
            rrow.append(float(val))
        ilist.append(rrow)
    print(ilist)


    startrow = 0
    endrow = 0
    nlist = []
    for index, row in enumerate(ilist):
        if row[0] == start:
            startrow = index
        if row[0] == end:
            endrow = index

    nlist = []
    while startrow <= endrow:
        nlist.append(ilist[startrow])
        startrow += 1
    print(nlist)

    #make string list

    solution = ["{}".format(row) for row in nlist]

    #print to file
    with open(targetFileName, 'w') as writefile:
        writefile.writelines(solution)

def getSampledSignal(signalName):
    lines = openFile('signals.txt')
    llist = [line.split() for line in lines]
    signals = llist[0][1:]
    print(signals)
    llist = llist[2:]
    #print(llist)

    if signalName in signals:
        sigindex = signals.index(signalName)
    else:
        return []

    for row in llist:
        #print(row[0])
        if type(row[0]) is int:
            print(row[0])
    return None

def identifyCheapest(componentSet):

    #build cdw dict
    lines = openFile('Sources/CDW.txt')
    llist = [line.split() for line in lines[3:]]
    cdwdict = {line[0] + ' ' + line[1]: float(line[3][1:]) for line in llist}
    #pp(cdwdict)

    #build eBay dict
    lines = openFile('Sources/eBay.txt')
    llist = [line.split() for line in lines[3:]]
    eBaydict = {line[0] + ' ' + line[1]: float(line[3][1:]) for line in llist}
    #pp(eBaydict)

    #build GovConnection dict
    lines = openFile('Sources/GovConnection.txt')
    llist = [line.split() for line in lines[3:]]
    govdict = {line[0] + ' ' + line[1]: float(line[3][1:]) for line in llist}
    #pp(govdict)

    #build Target dict
    lines = openFile('Sources/Target.txt')
    llist = [line.split() for line in lines[3:]]
    targetdict = {line[0] + ' ' + line[1]: float(line[3][1:]) for line in llist}
    #pp(targetdict)

    fdict = {}
    for part in componentSet:
        dlist = ['CDW', 'Ebay', "GovConnection", "Target"]
        plist = [cdwdict.get(part, 100000), eBaydict.get(part, 1000000), govdict.get(part, 1000000), targetdict.get(part, 1000000)]
        price = min(plist)
        company = plist.index(price)
        #print(part)

        fdict[part] = (price, dlist[company])
        #pp(fdict)

    return fdict

def getComponentsToAdd():
    #build cdw dict
    lines = openFile('Sources/CDW.txt')
    llist = [line.split() for line in lines[3:]]
    cdwdict = {line[0] + ' ' + line[1]: float(line[3][1:]) for line in llist}
    #pp(cdwdict)

    #build eBay dict
    lines = openFile('Sources/eBay.txt')
    llist = [line.split() for line in lines[3:]]
    eBaydict = {line[0] + ' ' + line[1]: float(line[3][1:]) for line in llist}
    #pp(eBaydict)

    #build GovConnection dict
    lines = openFile('Sources/GovConnection.txt')
    llist = [line.split() for line in lines[3:]]
    govdict = {line[0] + ' ' + line[1]: float(line[3][1:]) for line in llist}
    #pp(govdict)

    #build Target dict
    lines = openFile('Sources/Target.txt')
    llist = [line.split() for line in lines[3:]]
    targetdict = {line[0] + ' ' + line[1]: float(line[3][1:]) for line in llist}
    #pp(targetdict)

    totalset = {key for key in cdwdict.keys()}
    totalset.update({key for key in govdict.keys()})
    totalset.update({key for key in eBaydict.keys()})
    totalset.update({key for key in targetdict.keys()})

    cdwset = {key for key in cdwdict.keys()}
    govset = {key for key in govdict.keys()}
    ebayset = {key for key in eBaydict.keys()}
    targetset = {key for key in targetdict.keys()}

    dlist = [('CDW', cdwset), ('eBay', ebayset), ("GovConnection", govset), ("Target", targetset)]

    fdict = {}
    for c, cset in dlist:
        fdict[c] = totalset - cset


    return fdict


if __name__ == "__main__":

    #test 1
    components = {'Intel i7-4700HQ', 'Intel i7-6970HQ'}
    print(identifyCheapest(components))

    #test 2

    #test 5
    print(getComponentsToAdd())

      #test 3
    print(getSummary())

    #test 4
    print(getSampledSignal('ISO610'))

    #test 5
    saveContinuousData(6.0, 7.875, "Continousput.txt")