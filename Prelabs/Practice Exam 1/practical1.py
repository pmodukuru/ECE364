def openFile(filename):
    with open(filename, 'r') as File:
        lines = File.readlines()
    return lines

def validout_list(slist):
    # check rows
    checkset = set()
    for row in slist:
        checkset = set()
        for val in row:
            if val not in checkset:
                checkset.add(val)
            else:
                return False

    # check cols
    checkset = set()
    for row in zip(*slist):
        checkset = set()
        for val in row:
            if val not in checkset:
                checkset.add(val)
            else:
                return False

    return True


def isValidOutput(fileName):

    # TODO: Remove the "pass" before you add any code to this block.
    #open and read file
    lines = openFile(fileName)
    slist = [list(line[:-1]) for line in lines]

    #check rows
    checkset = set()
    for row in slist:
        checkset = set()
        for val in row:
            if val not in checkset:
                checkset.add(val)
            else:
                return False

    #check cols
    checkset = set()
    for row in zip(*slist):
        checkset = set()
        for val in row:
            if val not in checkset:
                checkset.add(val)
            else:
                return False

    return True

def isColumnPuzzle(fileName):

    # TODO: Remove the "pass" before you add any code to this block.
    lines = openFile(fileName)
    slist = [list(line[:-1]) for line in lines]

    #check rows
    for row in slist:
        if row[0] == '.':
            return True

    for row in zip(*slist):
        if row[0] == '.':
            return True

    return False

def solvePuzzle(sourceFileName, targetFileName):

    # TODO: Remove the "pass" before you add any code to this block.
    # open and read file
    lines = openFile(sourceFileName)
    lines[8] += "\n"
    slist = [list(line[:-1]) for line in lines]

    #create row list set
    rlist = []
    for line in slist:
        rlist.append({value for value in line if value != '.'})

    #create col list set
    clist = []
    for line in zip(*slist):
        clist.append({value for value in line if value != '.'})

    compset = {'1','2','3','4','5','6','7','8','9'}

    #find if col/row is missing
    miss = None
    if len(rlist[0]) < 9:
        miss = 'col'
    else:
        miss = 'row'

    solvelist = []
    if miss == 'col':
        for index, row in enumerate(rlist):
            diff = compset - row
            solvelist.append(replacePeriod(slist[index], diff))
    if miss == 'row':
        missrow = []
        for index, col in enumerate(clist):
            diff = compset - col
            missrow.extend(diff)
        for row in slist:
            if row[0] == '.':
                solvelist.append(missrow)
            else:
                solvelist.append(row)

    #make list of string
    fn = []
    for row in solvelist:
        fn.append(''.join(row) + "\n")

    with open(targetFileName, 'w') as writefile:
        writefile.writelines(fn)


def replacePeriod(row, val):
    nlist = []
    for i in row:
        if i == '.':
            nlist.extend(val)
        else:
            nlist.append(i)
    return nlist


def getCallersOf(phoneNumber):

    # TODO: Remove the "pass" before you add any code to this block.
    lines = openFile("ActivityList.txt")
    clist = [tuple(line.split()) for line in lines[2:]]
    #print(clist)

    #build called:callernum dict
    ccndict = {}
    for caller, called, dur in clist:
        if called not in ccndict.keys():
            ccndict[called] = []
        ccndict[called].append(caller)

    #print(ccndict)

    #build num:name dict
    lines = openFile("People.txt")
    clist = [tuple(line.split()) for line in lines[2:]]
    clist = [(last+' '+first, num) for last, first, _, num in clist]
    #print(clist)
    nndict = {num[1:]: name for name, num in clist}
    #print(nndict)

    #build unique sorted list
    sset = set()
    for called, caller in ccndict.items():
        if called == phoneNumber:
            for num in caller:
                sset.add(nndict[num[8:]])
    slist = list(sset)
    slist.sort()

    return slist

def getCallActivity():

    # TODO: Remove the "pass" before you add any code to this block.
    # build num:name dict
    lines = openFile("People.txt")
    clist = [tuple(line.split()) for line in lines[2:]]
    clist = [(last + ' ' + first, num) for last, first, _, num in clist]
    # print(clist)
    nndict = {num[1:]: name for name, num in clist}
    print(nndict)

    lines = openFile("ActivityList.txt")
    clist = [tuple(line.split()) for line in lines[2:]]


    durdict = {}
    for caller, called, dur in clist:
        name = nndict[caller[8:]]
        if not name in durdict.keys():
            durdict[name] = (0,(0,0))
       # durdict[name] = (durdict[name][0] + 1, timeadd(durdict[1], dur)


    return None


if __name__ == "__main__":

    #test 1
    print(isValidOutput("valid.sud"))
    print(isValidOutput("invalid1.sud"))
    print(isValidOutput("invalid2.sud"))

    #test 2
    print(isColumnPuzzle("open1.sud"))
    print(isColumnPuzzle("open2.sud"))
    print(isColumnPuzzle("valid.sud"))

    #test4
    print(getCallersOf("707-825-5871"))

    #test5
    print(getCallActivity())

    #test 3
    solvePuzzle("open1.sud", "testsolve1.sud")
    solvePuzzle("open2.sud", "testsolve2.sud")


