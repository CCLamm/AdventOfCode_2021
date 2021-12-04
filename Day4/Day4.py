from textwrap import wrap

class board:
    def __init__(self, arrBoard):
        self.arrBoard = arrBoard
        self.arrBoardStatus = [ [0 for x in range(len(arrBoard))] for y in range(len(arrBoard[0])) ] 
    # Takes a number as input, then marks that number if it exists, then checks if it means a win and then returns the sum of unchecked boards
    def setNumber(self, iNum):
        for x in range(len(self.arrBoard)):
            for y in range(len(self.arrBoard[x])):
                if self.arrBoard[x][y]==iNum:
                    self.arrBoardStatus[x][y] = 1
        if self.checkWin():
            return self.sumUnmarked()
        return 0
    # Checks if the board has 5 in a row in either rows or cols
    def checkWin(self):
        for arrRow in self.arrBoardStatus:
            if sum(arrRow)==len(self.arrBoard):
                return True
        arrBoardStatusTranspose = [[self.arrBoardStatus[j][i] for j in range(len(self.arrBoardStatus))] for i in range(len(self.arrBoardStatus[0]))]
        for arrRow in arrBoardStatusTranspose:
            if sum(arrRow)==len(self.arrBoard[0]):
                return True
        return False
    # Return sum of unmarked tiles in a board
    def sumUnmarked(self):
        iSum = 0
        for x in range(len(self.arrBoard)):
            for y in range(len(self.arrBoard[x])):
                if self.arrBoardStatus[x][y]==0:
                    iSum = iSum + self.arrBoard[x][y]
        return iSum

# Set a number on all boards in an array - return sum of unmarked tiles for the FIRST winning board, also remove the winning board ffrom the array to cover Part 2
def setNumberOnBoards(arrBoardsfn, iNum):
    finalResult = 0
    for myBoard in reversed(arrBoardsfn): 
        setResult = myBoard.setNumber(iNum) 
        if setResult!=0:
            arrBoardsfn.pop(arrBoardsfn.index(myBoard))
            finalResult = setResult
    return finalResult

# MAIN RUN CODE
arrBoards = []

with open("input.txt") as file:
    lNumbers = [int(x) for x in file.readline().split(",")]
    nextLine = file.readline()
    while nextLine:    
        nextLine = file.readline()
        arrBoard = []
        while len(nextLine)>1:    
            rowArray = [int(x) for x in wrap(nextLine, 3)]
            arrBoard.append(rowArray)
            nextLine = file.readline()
        arrBoards.append(board(arrBoard))

winResult = setNumberOnBoards(arrBoards, lNumbers[0])
while winResult==0:
    lNumbers.pop(0)
    winResult = setNumberOnBoards(arrBoards, lNumbers[0])

print("PART 1: ", (winResult * lNumbers[0]))

while len(arrBoards)>0:
    lNumbers.pop(0)
    winResult = setNumberOnBoards(arrBoards, lNumbers[0])

print("PART 2: ", (winResult * lNumbers[0]))
