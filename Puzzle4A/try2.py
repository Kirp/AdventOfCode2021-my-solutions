

def GetNumInString(stringer):
    toOut = stringer.split(" ")
    cleanExit = 0
    while(cleanExit == 0):
        popper = []
        for out in range(len(toOut)):
            if(toOut[out]== "" or toOut[out]== " "): 
                popper.append(out)
        if(len(popper)>0):
            cleanExit = 0
            toOut.pop(popper[0])
        else:
            cleanExit = 1

    return toOut
    

class BingoBoard:
    def __init__(self,boardNum):
        self.boardNum = boardNum
        self.boardDict = {}
        self.winDict = {}
        self.currentRow = 0
        self.hasWon = 0

    def AddRow(self, rowList):
        rowSplit = GetNumInString(rowList)
        for row in range(len(rowSplit)):
            namer = str(self.currentRow) +"x"+ str(row)
            self.boardDict[namer] = int(rowSplit[row])
            self.winDict[namer] = 0
        self.currentRow+=1

    def DisplayGameBoard(self):
        for x in range(5):
            #namer = str(x)+"x"+str(y)
            print(self.boardDict[str(x)+"x0"],self.boardDict[str(x)+"x1"],self.boardDict[str(x)+"x2"],self.boardDict[str(x)+"x3"],self.boardDict[str(x)+"x4"])
        
    
    def GetDrawnNumber(self, drawnNum):
        if self.hasWon == 1: return
        #in case theres a pesky space of carriage return
        drawnNum = int(drawnNum)
        #check if we have it here
        
        haveIt = 0
        location = ""
        for key in self.boardDict:
            if self.boardDict[key] == drawnNum:
                haveIt = 1
                location = key
                break
        if haveIt == 0: return 
        #print(location)
        self.winDict[location] = 1
        
        #then we check for wins
        locSplit = location.split("x")
        #print(locSplit)
        rowWinCounter = 0
        colWinCounter = 0
        for row in range(5):
            namer = str(row)+"x"+locSplit[1]
            rowWinCounter += self.winDict[namer]
        #print(rowWinCounter)
        for col in range(5):
            namer = locSplit[0]+"x"+str(col)
            colWinCounter += self.winDict[namer]
        #print(colWinCounter)
        if rowWinCounter>=5 or colWinCounter >=5:
            self.hasWon = 1
            return [self.boardNum, self.GetSumOfAllUnmarked()*drawnNum]
        return 

    def GetSumOfAllUnmarked(self):
        sumIt = 0
        for key in self.boardDict:
            if self.winDict[key] == 0:
                sumIt += self.boardDict[key]
        return sumIt
        


        
        



f = open("input.txt")
readed = f.readlines()

drawnNumbers = readed.pop(0).split(",")



boardList = []

for boarder in range(len(readed)):
    booker = boarder * 6 
    if booker+5 < len(readed):
        newBoard = BingoBoard(boarder)
        newBoard.AddRow(readed[booker+1])
        newBoard.AddRow(readed[booker+2])
        newBoard.AddRow(readed[booker+3])
        newBoard.AddRow(readed[booker+4])
        newBoard.AddRow(readed[booker+5])
        boardList.append(newBoard)

"""
print(type(boardList[0].GetDrawnNumber("92")))
print(type(boardList[0].GetDrawnNumber("76")))
print(type(boardList[0].GetDrawnNumber("82")))
print(type(boardList[0].GetDrawnNumber("2")))
print(type(boardList[0].GetDrawnNumber("53"))==int)
"""

feedBack = []
for nums in drawnNumbers:
    for player in boardList:
        reply = player.GetDrawnNumber(nums)
        #print(player.boardNum)
        #print(reply)
        if type(reply) == list:
            #print("Win!")
            feedBack.append(reply)
print(feedBack)







