


class Nodes:
    def __init__(self, name, connection):
        self.name = name
        self.connections =[]
        self.connections.append(connection)
    
    def AddConnections(self, newConnection):
        self.connections.append(newConnection)


#--
f = open("input0.txt")
readed = f.readlines()

cleaned = []
for read in readed:
    cleaned.append(read.split("\n")[0])
#--

def GetHighestIntPositionInList(intList):
    highestPosi = 0
    for elemCtr in range(len(intList)):
        if intList[elemCtr] > intList[highestPosi]:
            highestPosi = elemCtr
    return highestPosi

def GetScore(currentPathStr, scoreStr, pathList):
    #assume there are no invalid characters
    if scoreStr == "start":
        return -1
    if scoreStr == "end":
        return 2
    if scoreStr.isupper() == True:
        if pathList.count(scoreStr) > 0:
            return 1
        else: 
            return 3
    if pathList.count(scoreStr) > 0:
        return -1
    if currentPathStr.islower() and scoreStr.islower():
        return -1
    return 4


def GetScoreaAE(currentPathStr, scoreStr, pathList):
    #priotize small, large, End
    #assume there are no invalid characters
    if scoreStr == "start":
        return -1
    if scoreStr == "end":
        return 2
    if scoreStr.isupper() == True:
        if pathList.count(scoreStr) > 0:
            return 1
        else: 
            return 3
    if pathList.count(scoreStr) > 0:
        return -1
    if currentPathStr.islower() and scoreStr.islower():
        return -1
    return 4

def GetScoreaEA(currentPathStr, scoreStr, pathList):
    #priotize small, end, large
    #assume there are no invalid characters
    if scoreStr == "start":
        return -1
    if scoreStr == "end":
        return 3
    if scoreStr.isupper() == True:
        if pathList.count(scoreStr) > 0:
            return 1
        else: 
            return 2
    if pathList.count(scoreStr) > 0:
        return -1
    if currentPathStr.islower() and scoreStr.islower():
        return -1
    return 4


def GetScoreAaE(currentPathStr, scoreStr, pathList):
    #prioritize large, small, end
    #assume there are no invalid characters
    if scoreStr == "start":
        return -1
    if scoreStr == "end":
        return 2
    if scoreStr.isupper() == True:
        if pathList.count(scoreStr) > 0:
            return 1
        else: 
            return 4
    if pathList.count(scoreStr) > 0:
        return -1
    if currentPathStr.islower() and scoreStr.islower():
        return -1
    return 3

def GetScoreAEa(currentPathStr, scoreStr, pathList):
    #prioritize large, end, small
    #assume there are no invalid characters
    if scoreStr == "start":
        return -1
    if scoreStr == "end":
        return 2
    if scoreStr.isupper() == True:
        if pathList.count(scoreStr) > 0:
            return 1
        else: 
            return 4
    if pathList.count(scoreStr) > 0:
        return -1
    if currentPathStr.islower() and scoreStr.islower():
        return -1
    return 3




def GetScoreEAa(currentPathStr, scoreStr, pathList):
    #prioritize end, large, small
    #assume there are no invalid characters
    if scoreStr == "start":
        return -1
    if scoreStr == "end":
        return 4
    if scoreStr.isupper() == True:
        if pathList.count(scoreStr) > 0:
            return 1
        else: 
            return 3
    if pathList.count(scoreStr) > 0:
        return -1
    if currentPathStr.islower() and scoreStr.islower():
        return -1
    return 2


def GetScoreEaA(currentPathStr, scoreStr, pathList):
    #prioritize end, small, large
    #assume there are no invalid characters
    if scoreStr == "start":
        return -1
    if scoreStr == "end":
        return 4
    if scoreStr.isupper() == True:
        if pathList.count(scoreStr) > 0:
            return 1
        else: 
            return 2
    if pathList.count(scoreStr) > 0:
        return -1
    if currentPathStr.islower() and scoreStr.islower():
        return -1
    return 3


def ScoreUsingPattern(patternInt, currentPathStr, scoreStr, pathList):
    if patternInt == 0:
        return GetScoreaAE(currentPathStr, scoreStr, pathList)
    if patternInt == 1:
        return GetScoreaEA(currentPathStr, scoreStr, pathList)
    if patternInt == 2:
        return GetScoreAaE(currentPathStr, scoreStr, pathList)
    if patternInt == 3:
        return GetScoreAEa(currentPathStr, scoreStr, pathList)
    if patternInt == 4:
        return GetScoreEaA(currentPathStr, scoreStr, pathList)
    if patternInt == 5:
        return GetScoreEAa(currentPathStr, scoreStr, pathList)
    







#Main starts here
#fill up the list
nodeList = {}
for clean in cleaned:
    dataSplit = clean.split("-")
    try:
        nodeList[dataSplit[0]].append(dataSplit[1])
    except:
        nodeList[dataSplit[0]] = [dataSplit[1]]
    #and reverse
    try:
        nodeList[dataSplit[1]].append(dataSplit[0])
    except:
        nodeList[dataSplit[1]] = [dataSplit[0]]
print(nodeList)

#lets do the pathing
# first lets add the links from start
currentPathSteps = [["start"]]
currentNode = "start"
currentAvailablePaths = nodeList[currentNode]
howManyPaths = len(currentAvailablePaths)
for pathsCtr in range(howManyPaths):
    pathList = [currentNode]
    pathList.append(currentAvailablePaths[pathsCtr])
    if pathsCtr < len(currentAvailablePaths)-1:
        currentPathSteps[pathsCtr] = pathList
    else:
        currentPathSteps.append(pathList)
print(currentPathSteps)


endedPathList = []
for patternCtr in range(6):
    copyCurrentPathSteps = currentPathSteps.copy()
    for loopCtr in range(5):
        howManyPaths = len(copyCurrentPathSteps)
        for pathsCtr in range(howManyPaths):
            nodeLatestPath = copyCurrentPathSteps[pathsCtr]
            nodeLatestPath = nodeLatestPath[len(nodeLatestPath)-1]
            print("Latest Path: "+nodeLatestPath)  
            if nodeLatestPath == "end":
                continue
            try:  
                nodeAvailablePaths = nodeList[nodeLatestPath]
            except:
                nodeAvailablePaths = []
            print(nodeAvailablePaths)

            #lets score them
            scoreList = []
            for elem in nodeAvailablePaths:
                scoreList.append(ScoreUsingPattern(patternCtr,nodeLatestPath, elem, copyCurrentPathSteps[pathsCtr]))
            print(scoreList)
            highestScore = GetHighestIntPositionInList(scoreList)
            print(highestScore)
            chosenPath = nodeAvailablePaths[highestScore]
            print(chosenPath)
            
            #check if chosenPath has nodes other than current
            chosenPathCheck = nodeList[chosenPath]
            
            if len(chosenPathCheck) == 1:
                #reflect back
                copyCurrentPathSteps[pathsCtr].append(chosenPath)
                copyCurrentPathSteps[pathsCtr].append(nodeLatestPath)
            else:
                copyCurrentPathSteps[pathsCtr].append(chosenPath)
        #print(copyCurrentPathSteps)
    endedPathList += copyCurrentPathSteps
#print(endedPathList)
for ended in endedPathList:
    print(ended)   
