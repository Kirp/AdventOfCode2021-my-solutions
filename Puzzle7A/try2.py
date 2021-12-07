def stepGas(target):
    stepCount = 0
    for step in range(1, target+1):
        stepCount+=step
    return stepCount
    

def getHighestNumber(alist):
    currentHigh = 0
    for numb in alist:
        if numb > currentHigh:
            currentHigh = numb
    return currentHigh


def getLowestNumber(alist):
    currentLow = alist[0]
    for numb in alist:
        if numb > currentLow:
            currentHigh = numb
    return currentLow


def totalCrabGasSpentToGetToPosition(position, aubList):
    gasGuzzled = 0
    for crabIndex in range(len(aubList)):
        subPosition = aubList[crabIndex]
        gasSpent = 0
        if subPosition < position:
            gasSpent = position-subPosition
        else:
            gasSpent = subPosition-position
        guzzle = stepGas(gasSpent)
        #print("move from "+str(subPosition)+" to "+str(position)+": "+str(guzzle)+" fuel")
        gasGuzzled += guzzle
    return gasGuzzled


f = open("input.txt")
readed = f.readlines()

crabList = []
readed = readed[0].split(",")


for read in readed:
    crabList.append(int(read))

gasGuzList = []
highestPosition = getHighestNumber(crabList)

for pos in range(highestPosition):
    gasGuzList.append(totalCrabGasSpentToGetToPosition(pos, crabList))

gasGuzList.sort()
lowestGas = gasGuzList[0]
print(lowestGas)
    


#print("gasGuzzleTest: "+str(totalCrabGasSpentToGetToPosition(5, crabList)))
#print(stepGas(4))
    

