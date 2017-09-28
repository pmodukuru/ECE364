import re
from pprint import pprint as pp


def getWords(sentence, letter):
    regex = r'\b(#\w*[^#\W]|[^#\W]\w*#)\b'.replace('#', letter)
    return re.findall(regex, sentence, re.I)

def extractFloats(s):
    regex = r'[+-]?\d+\.\d+'
    return re.findall(regex, s)

def getUrlParts(url):
    #get base url
    regex = r'www.\w+.(edu|com|gov)'
    match = re.search(regex, url)
    base = match.group(0)

    #get controller
    regex = r'/\w+/'
    match = re.search(regex, url)
    control = match.group(0)[1:-1]

    #get action
    regex = r'/\w+\?'
    match = re.search(regex, url)
    action = match.group(0)[1:-1]

    return (base, control, action)

def getQueryParameters(url):
    #regex = r'(\w+=\w+)+'
    regex = r'(\w+[-._]?=\w+[-._]?\w+)+'
    match = re.findall(regex, url)
    l = []
    for param in match:
        #match parameter
        regex = r'\w+[-_.]?='
        match = re.findall(regex, param)
        query = match[0][:-1]
        #print(query)

        #match values
        regex = r'=\w+[-_.]?\w+'
        #regex = r'=.+'
        match = re.findall(regex, param)
        value = match[0][1:]
        #print(value)

        l.append((query, value))

    return l

def openFile(filename):
    with open(filename, 'r') as File:
        lines = File.readlines()
    return lines

def findFunctions(fileName):
    lines = openFile(fileName)

    regex = r'def.+'
    flist = []
    for line in lines:
        match = re.findall(regex,line)
        if match != []:
            reg = r'\w+'
            mat = re.findall(reg, match[0])
            #print(mat)

            name = mat[1]
            tlist = []
            for val in mat[2:]:
                #print(val)
                tlist.append(val)

            flist.append((name, tlist))

    return flist


if __name__ == "__main__":

    #test 1
    s = "The TART program runs on Tuesdays and Thursdays, but it does not start until next week."
    print(getWords(s, 't'))

    #test 2
    s1 = "The tires can tolerate temperatures between -32.5 and 110. That why they cost 149.95 dollars each."
    s2 = "The signal fluctuates between -0.3452 and +12.6509 volts. Try to keep it at 6 volts."
    print(extractFloats(s1))
    print(extractFloats(s2))

    #test 3
    url1 = "http://www.purdue.edu/Home/Calendar?Year=2016&Month=September&Semester=Fall"
    url2 = "http://www.google.com/Math/Constants?Pi=3.14&Max_Int=65536&What_Else=Nothing-Here"
    print(getUrlParts(url1))
    print(getUrlParts(url2))

    #test 4
    print(getQueryParameters(url1))
    print(getQueryParameters(url2))

    #test 5
    print(findFunctions('dataStructs.py'))


