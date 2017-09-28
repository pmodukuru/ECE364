def openFile(filename):
    with open(filename, 'r') as File:
        lines = File.readlines()
    return lines

def validout_list(slist):
    pass

def isValidOutput(fileName):

    # TODO: Remove the "pass" before you add any code to this block.
    sudoku = openFile(fileName)
    sudoku = [list(line.strip('\n')) for line in sudoku]
    #print(sudoku)

    #check rows
    for row in sudoku:
        if len(set(row)) < 9:
            return False

     #check cols
    for col in zip(*sudoku):
        if len(set(col)) < 9:
            return False

    return True


def isColumnPuzzle(fileName):

    # TODO: Remove the "pass" before you add any code to this block.
    sudoku = openFile(fileName)
    sudoku = [list(line.strip('\n')) for line in sudoku]

    comp = ('.', '.', '.', '.', '.', '.', '.', '.', '.')
    for col in zip(*sudoku):
        if col == comp:
            return True

    return False

def solvePuzzle(sourceFileName, targetFileName):

    # TODO: Remove the "pass" before you add any code to this block.

    #build list sudoku
    sudoku = openFile(sourceFileName)
    sudoku = [list(line.strip('\n')) for line in sudoku]
    #print(sudoku)

    #solve
    compset = {'1','2','3','4','5','6','7','8','9'}

    colpuzzle = isColumnPuzzle(sourceFileName)

    solution = []
    #missing col
    if colpuzzle:
        for row in sudoku:
            rowset = set(row)
            rowset.remove('.')
            diff = compset - rowset
            nrow = replacePeriod(row, diff)
            solution.append(nrow)
    #missing row
    else:
        missrow = []
        for col in zip(*sudoku):
            colset = set(col)
            colset.remove('.')
            diff = compset - colset
            missrow.extend(diff)

        #add miss row
        for row in sudoku:
            if row[0] == '.':
                solution.append(missrow)
            else:
                solution.append(row)


    #make string list
    solution = [''.join(row)+'\n' for row in solution]

    #print to file
    with open(targetFileName, 'w') as writefile:
        writefile.writelines(solution)

    return


def replacePeriod(row, diff):
    nrow = []
    for val in row:
        if val == '.':
            nrow.extend(diff)
        else:
            nrow.append(val)
    return nrow

def getCallersOf(phoneNumber):

    # TODO: Remove the "pass" before you add any code to this block.
    pass
def getCallActivity():

    # TODO: Remove the "pass" before you add any code to this block.
    pass

if __name__ == "__main__":
    #test 1
    print(isValidOutput("valid.sud"))
    print(isValidOutput("invalid1.sud"))
    print(isValidOutput("invalid2.sud"))

    #test 2
    print(isColumnPuzzle("open1.sud"))

    #test 3
    solvePuzzle("open2.sud", "test2solved")