
import re
from uuid import UUID
from pprint import pprint as pp


def openFile(filename):
    with open(filename, 'r') as File:
        lines = File.readlines()
    return lines

def formatname(name):
    regex = r'(\w+),\s(\w+)'
    nm = re.match(regex, name, re.I)
    if nm != None:
        last = nm.group(1)
        first = nm.group(2)
        return first + ' ' + last

    return name

def formatphone(num):
    regex = r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)'
    ph1 = re.match(regex, num, re.I)
    if ph1 != None:
        return '('+ph1.group(1)+') '+ph1.group(2)+'-'+ph1.group(3)

    #regex = r'(\d\d\d)(\d\d\d)(\d\d\d\d)'
    regex = r'\d{10}'
    ph2 = re.findall(regex, num, re.I)
    #print(ph2)
    if ph2 != []:
       # print(ph2)
        return '('+ph2[0][:3]+') '+ph2[0][3:6]+'-'+ph2[0][6:]
        #print(ph2)

    return num

def getRejectedEntries():
    lines = openFile("CompanyEmployees.txt")
    l = []
    for line in lines:
        regex = r'((\w+\s\w+)|(\w+,\s\w+))[,;\s]*$'
        match = re.match(regex, line, re.I)
        if match != None:
            l.append(formatname(match.group(1)))

    l.sort()

    return l

        #matlen1 = len(match)

        #regex = r'{\w+-\w+-\w+-\w+-\w+}|\w+-\w+-\w+-\w+-\w+|\w{32}'
        #match = re.findall(regex, line, re.I)
        #matlen2 = len(match)

        #regex = r'(\d{3})\s\d{3}-\d{4}'
        #match = re.findall(regex, line, re.I)
        #print(match)

def getCompleteEntries():
    iddict = getEmployeesWithIDs()
    phdict = getEmployeesWithPhones()
    stdict = getEmployeesWithStates()

    #build total set of names which have at least phone, state, or ID
    sset = [name for name in phdict.keys()]
    [sset.append(name) for name in stdict.keys()]
    [sset.append(name) for name in iddict.keys()]
    sset = set(sset)

    complete = {}
    #search through dict
    for name in sset:
        if iddict.get(name) == None or phdict.get(name) == None or stdict.get(name) == None:
            continue
        complete[name] = (iddict.get(name), phdict.get(name), stdict.get(name))

    return complete



def getEmployeesWithIDs():
    lines = openFile("CompanyEmployees.txt")
    d = {}
    for line in lines:
        #find names
        regex = r'((\w+\s\w+)|(\w+,\s\w+))'
        nm = re.search(regex, line, re.I)
        #print(nm.group(1))

        #find id
        regex = r'({\w+-\w+-\w+-\w+-\w+}|\w+-\w+-\w+-\w+-\w+|\w{32})'
        idn = re.search(regex, line, re.I)
        #print(idn)

        if nm != None and idn != None:
            d[formatname(nm.group(1))] = str(UUID(idn.group(1)))

    return d

def getEmployeesWithPhones():
    lines = openFile("CompanyEmployees.txt")
    d = {}
    for line in lines:
        #find names
        regex = r'((\w+\s\w+)|(\w+,\s\w+))'
        nm = re.search(regex, line, re.I)
        #print(nm.group(1))

        #find phone
        regex = r'(\(\d\d\d\)\s\d\d\d-\d\d\d\d|\d\d\d-\d\d\d-\d\d\d\d|\d{10})'
        ph = re.search(regex, line, re.I)
        #print(ph)

        if nm != None and ph != None:
            d[formatname(nm.group(1))] = formatphone(ph.group(1))

    return d

def getEmployeesWithStates():

    lines = openFile("CompanyEmployees.txt")
    d = {}
    for line in lines:
        #find names
        regex = r'((\w+\s\w+)|(\w+,\s\w+))'
        nm = re.search(regex, line, re.I)

        #find states
        regex = r'(([a-zA-Z]+\s[a-zA-Z]+)|[a-zA-Z]+)$'
        st = re.findall(r'([a-zA-Z]+\s[a-zA-Z]+|[a-zA-Z]+)$', line, re.I)

        if nm != None and st != []:
            d[formatname(nm.group(1))] = st[0]

    return d


def getEmployeesWithoutIDs():
    iddict = getEmployeesWithIDs()
    phdict = getEmployeesWithPhones()
    stdict = getEmployeesWithStates()

    #build total set of names which have at least phone, state, or ID
    sset = [name for name in phdict.keys()]
    [sset.append(name) for name in stdict.keys()]
    [sset.append(name) for name in iddict.keys()]
    sset = set(sset)

    noid = []
    #search through dict
    for name in sset:
        if iddict.get(name) == None:
            noid.append(name)

    noid.sort()
    return noid


def getEmployeesWithoutPhones():
    iddict = getEmployeesWithIDs()
    phdict = getEmployeesWithPhones()
    stdict = getEmployeesWithStates()

    #build total set of names which have at least phone, state, or ID
    sset = [name for name in phdict.keys()]
    [sset.append(name) for name in stdict.keys()]
    [sset.append(name) for name in iddict.keys()]
    sset = set(sset)

    noid = []
    #search through dict
    for name in sset:
        if phdict.get(name) == None:
            noid.append(name)

    noid.sort()
    return noid

def getEmployeesWithoutStates():
    iddict = getEmployeesWithIDs()
    phdict = getEmployeesWithPhones()
    stdict = getEmployeesWithStates()

    #build total set of names which have at least phone, state, or ID
    sset = [name for name in phdict.keys()]
    [sset.append(name) for name in stdict.keys()]
    [sset.append(name) for name in iddict.keys()]
    sset = set(sset)

    noid = []
    #search through dict
    for name in sset:
        if stdict.get(name) == None:
            noid.append(name)

    noid.sort()
    return noid

if __name__ == "__main__":

    #test 1
    print(getRejectedEntries())

    #test2
    #getEmployeesWithIDs()
    #pp(getEmployeesWithIDs())
    #print(len(getEmployeesWithIDs()))

    #test 3
    #pp(getEmployeesWithPhones())
    #pp(len(getEmployeesWithPhones()))

    #tet 4
    #pp(getEmployeesWithStates())
    #print(len(getEmployeesWithStates()))

    #test 5
    #pp(getEmployeesWithoutIDs())
    #print(len(getEmployeesWithoutIDs()))

    #test 6
    #pp(getEmployeesWithoutPhones())
    #print(len(getEmployeesWithoutPhones()))

    #test 7
    #pp(getEmployeesWithoutStates())
    #print(len(getEmployeesWithoutStates()))

    #test 8
    #pp(getCompleteEntries())
    #print(len(getCompleteEntries()))