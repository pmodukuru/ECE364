import re
from pprint import pprint as pp
import glob

def openFile(filename):
    with open(filename, 'r') as File:
        lines = File.readlines()
    return lines

def isNameValid(signalName):
    match = re.match(r'^[A-Z]{3}-[0-9]{3}$',signalName)
    if match != None:
        return True
    return False


def loadSignal(signalName, signalFolder):
    if isNameValid(signalName) == False:
        raise ValueError("{} is invalid".format(signalName))

    allfiles = glob.glob("./{0}/{1}.txt".format(signalFolder,signalName))

    if allfiles == []:
        raise OSError("{}.txt not found in {} folder".format(signalName,signalFolder))

    lines = openFile(allfiles[0])

    nfloat = 0
    flist = []

    for line in lines:
        match = re.match('[-]?[0-9]+.[0-9]+', line)
        if match == None:
            nfloat += 1
        else:
            flist.append(float(match.group(0)))

    return (flist, nfloat)


def isSignalAcceptable(signal, valueRange, maxCount):
    if len(signal) == 0:
        raise ValueError("Signal contains no data.")

    badcnt = 0
    for val in signal:
        if val < valueRange[0] or val > valueRange[1]:
            badcnt += 1

    if badcnt <= maxCount:
        return True

    return False



if __name__ == "__main__":
    #test 1
    print(isNameValid("AFE-996"))
    print(isNameValid("WAZE-386"))
    print(isNameValid("XYZ-2020"))

    #test 2
    v, c = loadSignal("REY-386", "Signals")
    pp(len(v))
    print(c)

    #test 3
    v, c = loadSignal("REY-386", "Signals")
    print(isSignalAcceptable(v, (-12.0, 11.7), 5))

    v, c = loadSignal("REY-386", "Signals")
    print(isSignalAcceptable(v, (-12.0, 11.7), 20))