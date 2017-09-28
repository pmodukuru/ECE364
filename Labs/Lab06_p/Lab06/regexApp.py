#! /usr/local/bin/python3.4
import re
from uuid import UUID

def loadFile(x):

    with open(x, "r") as signalFile:
        lines = signalFile.readlines()

    return lines


def getAll():
    input = loadFile("CompanyEmployees.txt")
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
    #input = loadFile("CompanyEmployees.txt")
    #print(input)
    #result=[]
    #getAll()
    #for x in input:
        #name = re.findall("\w+, \w+|\w+ \w+"+",",x)
        #print(name)
        #if re.match('\w+, \w+,|\w+ \w+'+'[,; ]+',x):
     #   if re.match(r'(\w+, \w+|\w+ \w+)([,;\s]+)$',x):
      #      name = re.findall("\w+, \w+|\w+ \w+",x)
       #     if re.match(r'\w+, \w+',name[0]):
        #        temp = re.findall("\w+",name[0])
                #print(temp)
         #       name[0]=temp[1]+" "+temp[0]

#            result.append(name[0])



        #print(name)
    #Jody, Clark,, , ;,; ;,; ;,;, ;,; ,,
    #print(sorted(result))


    input=getAll()
    #print(input[78])
    result=[]
    for name,Id,phone,state in input:
        if Id=="" and phone=="" and state=="":
            result.append(name)

    #print(len(result))
    return sorted(result)


def getCompleteEntries():
    input=getAll()
    #print(input[78])
    result={}
    for name,Id,phone,state in input:
        if Id!="" and phone!="" and state!="":
            result[name]=(Id,phone,state)

    #print(len(result))
    #print(result["Watkins Chester"])
    return result


def getEmployeesWithIDs():
    input=getAll()
    result={}
    for name,Id,phone,state in input:
        if Id!="":
            result[name]=Id

    #print(len(result))
    #print(result["Houston Calvin"])
    return result



def getEmployeesWithPhones():
    # input = loadFile("CompanyEmployees.txt")
    # result={}
    # for x in input:
    #     y = re.findall(r',(([0-9]{10})|(\([0-9]{3}\) [0-9]{3}-[0-9]{4})|([0-9]{3}-[0-9]{3}-[0-9]{4}))',x)
    #     #if re.match(r'[0-9]{10}',x):
    #     if y is not None and len(y) >0:
    #         #print(y)
    #
    #         name = re.findall("\w+, \w+|\w+ \w+",x)
    #         number=y[0][0]
    #         digits = re.findall(r"\d", number)
    #         #print(digits)
    #         phone= "("+digits[0]+digits[1]+digits[2]+")"+" "+digits[3]+digits[4]+digits[5]+"-"+digits[6]+digits[7]+digits[8]+digits[9]
    #         #print(phone)
    #         #print(name)
    #         if re.match(r'\w+, \w+',name[0]):
    #             temp = re.findall("\w+",name[0])
    #             #print(temp)
    #             name[0]=temp[1]+" "+temp[0]
    #         result[name[0]]=phone
    # #print(result["Houston Calvin"])
    # #print(len(result))
    input=getAll()
    result={}
    for name,Id,phone,state in input:
        if phone!="":
            result[name]=phone

    #print(len(result))
    #print(result["Houston Calvin"])
    return result



def getEmployeesWithStates():
    input=getAll()
    result={}
    for name,Id,phone,state in input:
        if state!="":
            result[name]=state

    #print(len(result))
    #print(result["Sandra Robertson"])
    return result


def getEmployeesWithoutIDs():
    input=getAll()
    reject=getRejectedEntries()
    result=[]
    for name,Id,phone,state in input:
        if Id=="" and name not in reject:
            result.append(name)

    #print(len(result))
    #print(result["Houston Calvin"])
    return sorted(result)


def getEmployeesWithoutPhones():
    # valid =  getEmployeesWithPhones()
    # input = loadFile("CompanyEmployees.txt")
    # nval = getRejectedEntries()
    # result=[]
    # #print(type(valid))
    # for x in input:
    #     name = re.findall("\w+, \w+|\w+ \w+",x)
    #     if re.match(r'\w+, \w+',name[0]):
    #             temp = re.findall("\w+",name[0])
    #             #print(temp)
    #             name[0]=temp[1]+" "+temp[0]
    #     #print(name)
    #     if name[0] not in valid and name[0] not in nval:
    #         result.append(name[0])
    # #print(result)
    # #print(len(result))
    #return result
    input=getAll()
    reject=getRejectedEntries()
    result=[]
    for name,Id,phone,state in input:
        if phone=="" and name not in reject:
            result.append(name)

    #print(len(result))
    return sorted(result)

def getEmployeesWithoutStates():
    input=getAll()
    reject=getRejectedEntries()
    result=[]
    for name,Id,phone,state in input:
        if state=="" and name not in reject:
            result.append(name)

    #print(len(result))
    return sorted(result)




if __name__ == "__main__":


    print(getRejectedEntries())
    print(getEmployeesWithIDs())
    print(getEmployeesWithPhones())
    print(getEmployeesWithStates())
    print(getEmployeesWithoutIDs())
    print(getEmployeesWithoutPhones())
    print(getEmployeesWithoutStates())
    print(getCompleteEntries())
