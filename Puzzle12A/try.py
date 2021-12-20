



#--
f = open("input.txt")
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

def GetScore(currentPathStr, scoreStr, pathList, nodes):
    #assume there are no invalid characters
    if scoreStr == "start":
        return -1
    if scoreStr == "end":
        return 2
    if len(nodes[scoreStr]) == 1:
        #check if this path was used before
        if scoreStr.isupper() == True:
            """
            for pathCtr in range(len(pathList)):
                path = pathList[pathCtr]
                if path == scoreStr:
                    if pathCtr < len(pathList)-1:
                        if pathList[pathCtr+1]==currentPathStr:
                            return -1
            """            
            return -1
        
        if currentPathStr.islower() and scoreStr.islower():
            return -1

                

    if scoreStr.isupper() == True:
        return 3
    if pathList.count(scoreStr) > 0:
        return -1
    #if currentPathStr != "start":
    #    if currentPathStr.islower() and scoreStr.islower():
    #        return -1
    
    return 4



def RunPathSearchPattern(patternInt, pathTakenList, nodes):
    unfollowedPaths = []
    antiLoop = 0
    #print("starting with:")
    #print(pathTakenList)

    while antiLoop < 1000:
        antiLoop+=1
        #print("loop: "+str(antiLoop))
        currentNode = pathTakenList[len(pathTakenList)-1]
        #print("currentNode: "+currentNode)
        pathways = nodeList[currentNode]
        if currentNode == "end":
            return [pathTakenList, unfollowedPaths]
        scoreList = []
        for elem in pathways:
            scoreList.append(GetScore(currentNode, elem, pathTakenList, nodes))
        #print("find highest score")
        #print(pathways)
        #print(scoreList)
        
        deadEndCheck = scoreList.count(-1)
        #print("deadEndCheck: "+str(deadEndCheck))
        if deadEndCheck == len(scoreList):
            return [[],unfollowedPaths]
        highestScore = GetHighestIntPositionInList(scoreList)
        #print(highestScore)
        
        chosenPath = pathways[highestScore]
        #print(chosenPath)
        for unfollowCtr in range(len(pathways)):
            unFollow = pathways[unfollowCtr]
            unFollowScore = scoreList[unfollowCtr]
            if unFollow != chosenPath and unFollowScore>0:
                unPathway = pathTakenList.copy()
                unPathway.append(unFollow)
                unfollowedPaths.append(unPathway)
        
        pathTakenList.append(chosenPath)
        #print("updated path")
        #print(pathTakenList)
        #print("rejected paths")
        #print(unfollowedPaths)
    return "rejected"

    






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
acceptedPaths = []
currentPathSteps = ["start"]
currentNode = "start"
allRejects = []

loopCtr = 0
while loopCtr < 1000:
    loopCtr +=1
    patternResult = RunPathSearchPattern(0, currentPathSteps, nodeList)
    rejectedList = patternResult[1]
    if len(patternResult[0])>0:
        acceptedPaths.append(patternResult[0])
    #take out the rejected with 'end'
    for reject in rejectedList:
        if reject[len(reject)-1] == "end":
            if(acceptedPaths.count(reject)==0):
                acceptedPaths.append(reject)
        else:
            if(allRejects.count(reject)==0):
                allRejects.append(reject)
    if len(allRejects) == 0:
        loopCtr = 1001
    else:
        currentPathSteps = allRejects.pop()
        

print("all done")
print("final accepted paths")
print(len(acceptedPaths))
#for paths in acceptedPaths:
#    print(paths)




























"""
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
    print(copyCurrentPathSteps)
    for loopCtr in range(5):
        howManyPaths = len(copyCurrentPathSteps)
        for pathsCtr in range(howManyPaths):
            nodeLatestPath = copyCurrentPathSteps[pathsCtr]
            nodeLatestPath = nodeLatestPath[len(nodeLatestPath)-1]
            #print("Latest Path: "+nodeLatestPath)  
            if nodeLatestPath == "end":
                continue
            try:  
                nodeAvailablePaths = nodeList[nodeLatestPath]
            except:
                nodeAvailablePaths = []
            #print(nodeAvailablePaths)

            #lets score them
            scoreList = []
            for elem in nodeAvailablePaths:
                scoreList.append(ScoreUsingPattern(patternCtr,nodeLatestPath, elem, copyCurrentPathSteps[pathsCtr]))
            #print(scoreList)
            highestScore = GetHighestIntPositionInList(scoreList)
            #print(highestScore)
            chosenPath = nodeAvailablePaths[highestScore]
            #print(chosenPath)
            
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
"""   
