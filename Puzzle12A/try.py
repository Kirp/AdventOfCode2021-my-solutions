


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

def GetScore(scoreStr, pathList):
    #assume there are no invalid characters
    if scoreStr == "start":
        return -1
    if scoreStr == "end":
        return 1
    if scoreStr.isupper() == True:
        return 2
    if pathList.count(scoreStr) > 0:
        return -1
    return 3






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

howManyPaths = len(currentAvailablePaths)
for pathsCtr in range(howManyPaths):
    nodeLatestPath = currentAvailablePaths[pathsCtr]
    nodeLatestPath = nodeLatestPath[len(nodeLatestPath)-1]
    print("Latest Path: "+str(nodeLatestPath))  
    try:  
        nodeAvailablePaths = nodeList[nodeLatestPath]
    except:
        nodeAvailablePaths = []
    print(nodeAvailablePaths)

    #lets score them
    scoreList = []
    for elem in nodeAvailablePaths:
        scoreList.append(GetScore(elem, nodeAvailablePaths))
    print(scoreList)
    highestScore = GetHighestIntPositionInList(scoreList)
    print(highestScore)
    chosenPath = nodeAvailablePaths[highestScore]
    print(chosenPath)

    #check if chosenPath has nodes 
    try:
        chosenPathCheck = nodeList[chosenPath]

    except:
        pass
