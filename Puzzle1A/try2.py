
f = open("subInput.txt")
readed = f.readlines()
lastMeasure = 0
midMeasure = 0
currentMeasure = 0
depth = 0

bypasser = 0
for x in readed:
    if bypasser > 2:
        print("do stuff")
    currentMeasure = int(x)
    midMeasure += currentMeasure
    lastMeasure += midMeasure
    
    
    bypasser +=1
    




