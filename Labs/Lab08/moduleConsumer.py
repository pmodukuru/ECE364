from moduleTasks import *

def loadSignals(signalNames, signalFolder, maxNonfloatCount):
    sdict = {}
    for signal in signalNames:
        try:
            v,c = loadSignal(signal, signalFolder)
            if c > maxNonfloatCount:
                sdict[signal] = []
            else:
                sdict[signal] = v
        except:
            sdict[signal] = None

    return sdict


def saveSignals(signalsDictionary, valueRange, maxCount, targetFolder):

    for signal, vals in signalsDictionary.items():
        if vals == None or len(vals) == 0:
            continue

        if (isSignalAcceptable(vals, valueRange, maxCount)):
            s = buildoutString(vals)
            writeFile(signal, targetFolder, s)


def buildoutString(vals):
    s = str(vals[0])
    for val in vals:
        temp = "{0:.3f}".format(val)
        s = s + '\n'+ temp

    return s

def writeFile(filename, folder, lines):
    with open('{0}/{1}.txt'.format(folder, filename), 'w') as myFile:
        myFile.writelines(lines)



if __name__ == "__main__":
    #test 1
    signals = ["AFW-481","CIG-308","FPT-701","GUO-758", "AFW-411", "AFW-4012", "REY-386"]
    pdict = loadSignals(signals, 'Signals', 20)


    #test 2
    #pp(pdict)
    saveSignals(pdict, (-12.0, 11.7), 20, 'test')