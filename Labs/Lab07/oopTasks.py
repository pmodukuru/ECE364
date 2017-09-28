from pprint import pprint as pp

def openFile(filename):
    with open(filename, 'r') as File:
        lines = File.readlines()
    return lines


class Experiment:

    def __init__(self, experimentNo, experimentDate, virusName, unitCount, unitCost):
        self.experimentNumber = experimentNo
        self.experimentDate = experimentDate
        self.virusName = virusName
        self.unitCount = unitCount
        self.unitCost = unitCost
        self.totalCost = self.unitCount * self.unitCost

    def __str__(self):
        return "{0:03d}, {1}, ${2:06.2f}: {3}".format(self.experimentNumber, self.experimentDate, self.totalCost, self.virusName)


class Technician:

    def __init__(self, techName, techID):
        self.techName = techName
        self.techID = techID
        self.experiments = {}

    def __str__(self):
        return "{0}, {1}: {2:02d} Experiments".format(self.techID, self.techName, len(self.experiments))

    def addExperiment(self, experiment):
        self.experiments[experiment.experimentNumber] = experiment

    def getExperiment(self, expNo):
        return self.experiments.get(expNo)

    def loadExperimentsFromFile(self, fileName):
        lines = openFile(fileName)

        for line in lines[2:]:
            collist = line.split()
            texp = Experiment(int(collist[0]), collist[1], collist[2], int(collist[3]), float(collist[4][1:]))
            self.addExperiment(texp)

    def generateTechActivity(self):
        slist = ["{0}, {1}".format(self.techID, self.techName)]

        #build exp list
        elist = ["{0:03d}, {1}, ${2:06.2f}: {3}".format(key, val.experimentDate, val.totalCost, val.virusName) for key, val in self.experiments.items()]
        elist.sort()

        slist.extend(elist)
        return '\n'.join(slist)

class Laboratory:

    def __init__(self, labName):
        self.labName = labName
        self.technicians = {}

    def __str__(self):
        slist = ["{0}: {1:02d} Technicians".format(self.labName, len(self.technicians))]

        tlist = ["{0}, {1}: {2:02d} Experiments".format(val.techID, val.techName, len(val.experiments)) for key, val in self.technicians.items()]
        tlist.sort()
        slist.extend(tlist)

        return "\n".join(slist)



    def addTechnician(self, technician):
        self.technicians[technician.techName] = technician

    def getTechnicians(self, *args):
        return [self.technicians[arg] for arg in args]

    def generateLabActivity(self):
        s = ""
        for name in sorted(list(self.technicians.keys())):
            tech = self.technicians[name]
            s = s + "\n" + "\n" + tech.generateTechActivity()

        return s[2:]


if __name__ == '__main__':

    #test exp
    e1 = Experiment(31, "04/01/2015", "commoncold", 5, 5)
    #print(e1)

    #test tech
    e2 = Experiment(32, "04/02/2015", "hi", 3, 19)
    e3 = Experiment(21, "04/02/2015", "hi", 3, 19)

    t1 = Technician("Irene Adler", "69069-29232")
    #pp(t1.experiments)
    t1.addExperiment(e1)
    t1.addExperiment(e2)
    t1.addExperiment(e3)
    #pp(t1.experiments)
    #print(t1.getExperiment(4))
    #print(t1)

    #print(t1.generateTechActivity())
    #print()
    t1.loadExperimentsFromFile('report 55926-36619.txt')
    #print(t1.generateTechActivity())

    #test lab
   # print()
    l1 = Laboratory("Eli Lilly")
    #print(l1.labName)
    #print(l1.technicians)
    l1.addTechnician(t1)
    #print(l1.technicians)

    t1 = Technician("Irene Adler", "69069-29232")
    t2 = Technician("Prady Modukuru", "00271-13993")
    t3 = Technician("Priya Raju", "18971-17733")

    t1.loadExperimentsFromFile('report 55926-36619.txt')
    t2.loadExperimentsFromFile("report 69069-29232.txt")
    t3.loadExperimentsFromFile("report 75471-28954.txt")

    l1.addTechnician(t1)
    l1.addTechnician(t2)
    l1.addTechnician(t3)

    #print(l1.getTechnicians('Prady Modukuru', 'Irene Adler'))

    #print(l1)

    print(l1.generateLabActivity())


