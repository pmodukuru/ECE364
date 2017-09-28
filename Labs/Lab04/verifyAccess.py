def loadFile(filename):

    with open("{}.txt".format(filename), "r") as signalFile:
        lines = signalFile.readlines()

    return lines


def getUserPermissions():
    #inits
    pdict = {}
    nmdict = {}

 #build id to access dict
    file = loadFile("Permissions")
    for line in file[2:]:
        row = line.split()
        #print(row)
        if not row[0] in pdict.keys():
            pdict[row[0]] = set()
            pdict[row[0]].add(row[2])

        else:
            pdict[row[0]].add(row[2])

    #build name-permission dict
    file = loadFile("AccessCards")
    for line in file[2:-1]:
        row = line.split()
        if row[3] in pdict.keys():
            nmdict[row[0]+' ' +row[1]] = pdict[row[3]]

    #test
    #print(nmdict["Young, Frank"])

    return nmdict


def getFloorPermissions():
    nmdict = getUserPermissions()
    floordict = {}
    for name, rooms in nmdict.items():
        for room in rooms:
            if not room in floordict:
                floordict[room] = set()
                floordict[room].add(name)
            else:
                floordict[room].add(name)

    #test
    #print(floordict["Equipments"])

    return floordict

def getFloorRooms():
    roomdict = {}
    file = loadFile("AccessLog")
    for line in file[:]:
        row = line.split(" - ")
        froom = row[1].split("-")
        if not froom[0] in roomdict.keys():
            roomdict[froom[0]] = set()
            roomdict[froom[0]].add(froom[1][:-1])

        else:
            roomdict[froom[0]].add(froom[1][:-1])

    #test
    #print(roomdict["Basement"])

    return roomdict

def isAccessGrantedFor(userName, attempt):
    floordict = getFloorPermissions()
    roomdict = getFloorRooms()

    tuplelist = checkAttempts()

    for name, floor, room, bool in tuplelist:
        if name == userName and floor == attempt[0] and room == attempt[1]:
            return bool
    return False

def checkAttempts():
    nmIDdict = {}
    tuplelist = []
    #tup = ()


    #build name-permission dict
    file = loadFile("AccessCards")
    for line in file[2:-1]:
        row = line.split()
        nmIDdict[row[3]] = row[0]+' ' +row[1]

    floordict = getFloorPermissions()
    roomdict = getFloorRooms()

    file = loadFile("AccessLog")
    for line in file:
        row = line.split(" - ")
        #print(row)
        name = nmIDdict[row[0]]
        floorrm = row[1].split("-")
        floor = floorrm[0]
        room = floorrm[1][:-1]

        if name in floordict[floor] and room in roomdict[floor]:
            tuplelist.append((name, floor, room, True))
        else:
            tuplelist.append((name, floor, room, False))

    return tuplelist

def getAttemptsOf(userName):
    alist = []
    tuplelist = checkAttempts()

    for name, floor, room, bool in tuplelist:
        if name == userName:
            alist.append((floor, room, bool))
    alist.sort()

    return alist

def getUserAttemptSummary():
    tuplelist = checkAttempts()
    attdict = {}
    cnt = 0
    fail = 0
    for name, floor, room, bool in tuplelist:
        if not name in attdict.keys():
            attdict[name] = tuple()
            attdict[name] = (0,0)
        else:
            tup = attdict[name]
            if bool == True:
                attdict[name] = (tup[0]+1, tup[1])
            else:
                attdict[name] = (tup[0], tup[1]+1)
    #print("hello")
    #print(attdict)
    return attdict

def getFloorAttemptSummary():
    pass


def getRoomAttemptSummary():
    pass

if __name__ == "__main__":
    print(getUserPermissions())

    print(getFloorPermissions())
    print(getFloorRooms())

    print(checkAttempts())

    print(isAccessGrantedFor('River, Patricia', ('Servers', 'Room46')))
    print(isAccessGrantedFor('Reed, Bobby', ('Equipments', 'Room86')))

    print(getAttemptsOf("Gray, Tammy"))
    print(getUserAttemptSummary())