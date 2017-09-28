import re
from pprint import pprint as pp

def openFile(filename):
    with open(filename, 'r') as File:
        lines = File.readlines()
    return lines

def getWords(sentence, letter):
    regex = r'\b(#\w*[^#\W]|[^#\W]\w*#)\b'.replace('#',letter)
    match = re.findall(regex, sentence, re.I)

    return match
def extractFloats(s):
    match = re.findall(r'[+-]?\d*\.\d+', s)
    return match

def getUrlParts(url):
    match = re.search(r'//([\w.-_]+)/([\w.-_]+)/([\w.-_]+)\?',url, re.I)
    return match.groups()

def getQueryParameters(url):
    match = re.findall(r'([\w._-]+)=([\w._-]+)',url)
    return match

def findFunctions(filename):
    file = openFile(filename)
    ls = []

    for line in file:
        match = re.search(r'def\s+([\w_]+)\(([\w\s,]+)\)',line)
        if match:
            pmatch = re.findall(r'\w+',str(match.group(2)))
            ls.append((match.group(1),pmatch))
    return ls

if __name__ == "__main__":
    #test 1
    s = "The TART program runs on Tuesdays and Thursdays, but it does not start until next week."
    print(getWords(s, 't'))

    # test 2
    s1 = "The tires can tolerate temperatures between -32.5 and 110. That why they cost 149.95 dollars each."
    s2 = "The signal fluctuates between -0.3452 and +12.6509 volts. Try to keep it at 6 volts."
    print(extractFloats(s1))
    print(extractFloats(s2))

    # test 3
    url1 = "http://www.purdue.edu/Home/Calendar?Year=2016&Month=September&Semester=Fall"
    url2 = "http://www.google.com/Math/Constants?Pi=3.14&Max_Int=65536&What_Else=Nothing-Here"
    print(getUrlParts(url1))
    print(getUrlParts(url2))

    # test 4
    print(getQueryParameters(url1))
    print(getQueryParameters(url2))

    # test 5
    pp(findFunctions('dataStructs.py'))