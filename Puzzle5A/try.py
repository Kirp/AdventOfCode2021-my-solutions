
f = open("input.txt")
readed = f.readlines()
print(len(readed))
print(readed[0])

mapDict = {}
crossCount = 0
#lets populate it with 0
for y in range(0,1000):
    for x in range(0,1000):
        namer = str(x)+"x"+str(y)
        mapDict[namer] = 0

for read in readed:
    splitter = read.split(" -> ")
    vect1 = splitter[0].split(",")
    vect2 = splitter[1].split(",")
    #print(vect1)
    #print(vect2)
    
    isLevelx = 0
    isLevely = 0

    if int(vect1[0]) == int(vect2[0]):
        isLevelx = 1
    if int(vect1[1]) == int(vect2[1]):
        isLevely = 1
    #only consider straight lines
    if isLevelx == 1 or isLevely == 1:
        print(read + " is valid")
        start = 0
        end = 0
        positionToUse = 0
        if isLevelx == 1:
            positionToUse = 1
        if int(vect1[positionToUse])>int(vect2[positionToUse]):
            start = int(vect2[positionToUse])
            end = int(vect1[positionToUse])+1
        else:
            start = int(vect1[positionToUse])
            end = int(vect2[positionToUse])+1
        for ctr in range(start, end):
            namer = ""
            if isLevelx == 1:
                namer = vect1[0]+"x"+str(ctr)
            else:
                namer = str(ctr)+"x"+vect1[1]
            #print(namer)
            mapDict[namer] +=1

            #if mapDict[namer]>1:
                #print("cross on "+namer+" for "+ str(mapDict[namer])+ "times")
            #    crossCount+=1

for coord in mapDict:
    if mapDict[coord] > 1:
        crossCount+=1

print(str(crossCount)+" crossed")


