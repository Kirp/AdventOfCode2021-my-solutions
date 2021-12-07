
def spawnMain(start, daysToRun):

    spawnTime = 7

    #print("starting at count "+str(start)+" with run time of "+str(daysToRun)+" days")
    if spawnTime > daysToRun:
        print("not enough time to spawn with "+ str(daysToRun) + " days left")
        return []
    computedChildren = 0
    firstSpawn = daysToRun - start
    if(start>0):
        computedChildren+=1
    print("first spawn at "+str(firstSpawn))
    modulod = firstSpawn%spawnTime
    spawnRunTime = firstSpawn - modulod
    print("spawnruntime : "+str(spawnRunTime))
    computedChildren += spawnRunTime/spawnTime
    print("computed children :"+str(computedChildren))
    return [firstSpawn, computedChildren]



def spawnChildren(runTime, numberOfChildren):
    #how many newly spawned had time to spawn
    remainingTime = runTime
    possibleChildren = []
    for chld in range(1,numberOfChildren+1):
        
        
        timeLeft = remainingTime - 8 * chld 
        print("child "+str(chld)+" spawn time left "+str(timeLeft))
        if timeLeft>7:
            modul = timeLeft%7
            #print(modul)
            mySpawnTime = timeLeft-modul
            #print(mySpawnTime)
            myChildren = mySpawnTime/7
            #print("possible children :"+str(myChildren))
            if myChildren > 0: 
                possibleChildren.append([timeLeft, myChildren])
    return possibleChildren

        
    
    
    



f = open("input0.txt")
readed = f.readlines()

fishList = []

for fish in readed[0].split(","):
    fishList.append(int(fish))
    #fishString+=fish



daysToSimulate = 18


"""
print("days to simulate: "+str(daysToSimulate))
childCount = 0
spawns = []
for toSpawn in fishList:
    result = spawnMain(toSpawn, daysToSimulate)
    if len(result)>0:
        spawns.append(spawnMain(toSpawn, daysToSimulate))
print("total Spawns: ")
print(spawns)
for spawn in spawns:
    childCount+=spawn[1]
print("childcount :"+str(childCount))
"""



bleeb = spawnMain(4, 18)
print(bleeb)

#bleeb = spawnMain(1, 7)
#print(bleeb)


"""
further = spawnChildren(bleeb[0],bleeb[1])
print(further)
print(len(further))
"""