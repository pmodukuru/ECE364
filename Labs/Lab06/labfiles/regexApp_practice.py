import re
from uuid import UUID
from pprint import pprint as pp

def openFile(filename):
    with open(filename, 'r') as File:
        lines = File.readlines()
    return lines

def getAll():
    input = openFile("CompanyEmployees.txt")
    result_all=[]

    for x in input:
        result_temp=[]
        name = re.findall("([A-za-z]+)(,?) ([A-za-z]+)",x)
        #print(name)
        temp = name[0]
        if temp[1] == ',':
            result_temp.append(temp[2]+" "+temp[0])
        else:
            result_temp.append(temp[0]+" "+temp[2])

        ID = re.findall("(\w{8})-?(\w{4})-?(\w{4})-?(\w{4})-?(\w{12})",x)
        #print(ID)

        if len(ID) == 0:
            result_temp.append("")
        else:
            ID_num = ID[0]
            temp = ""
            for i in ID_num:
                temp = temp + i
                #print(temp)
            result_temp.append(str(UUID(temp)))

        phone = re.findall("\(?([0-9]{3})\)?[- ]?([0-9]{3})-?([0-9]{4})",x)
        #print(phone)

        if len(phone) == 0:
            result_temp.append("")
        else:
            phone_num = phone[0]
            temp = "("+phone_num[0]+") "+phone_num[1]+"-"+phone_num[2]
            #print(temp)
            result_temp.append(temp)

        state = re.findall("([A-za-z]+ ?[A-za-z]*)$",x)
        #print(state)
        if len(state) == 0:
            result_temp.append("")
        else:
            result_temp.append(state[0])
        result_all.append(result_temp)
    #print(result_all)

    return result_all


def getRejectedEntries():
    file = openFile("CompanyEmployees.txt")
    ls = []
    for line in file:
        match = re.search(r'^(\w+,\s\w+|\w+\s\w+)[;,\s]*$',line)

    pass

if __name__ == "__main__":

    #test getrejected
    print(getRejectedEntries())

    pp(getAll())