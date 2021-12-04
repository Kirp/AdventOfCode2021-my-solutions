import re


def stringBinaryToInt(strb):
    toOut = 0
    size = len(strb)
    for ctr in range(size):
        rev = size - ctr -1
        toOut += int(strb[ctr]) * pow(2,rev)
    return toOut

def getMostCommon(base):
    commonList = [0,0,0,0,0,0,0,0,0,0,0,0]
    mostCommonBinList = [0,0,0,0,0,0,0,0,0,0,0,0]
    for read in base:
        for ctr in range(len(read)):
            if read[ctr]=="1":
                commonList[ctr]+=1
    #print(commonList)
    for ctr2 in range(len(commonList)):
        oneCount = commonList[ctr2]
        zeroCount = len(base) - oneCount
        if oneCount>zeroCount:
            mostCommonBinList[ctr2] = 1
        else: 
            mostCommonBinList[ctr2] = 0
    return mostCommonBinList


def getMostCommonOxy(base):
    commonList = [0,0,0,0,0,0,0,0,0,0,0,0]
    mostCommonBinList = [0,0,0,0,0,0,0,0,0,0,0,0]
    for read in base:
        for ctr in range(len(read)):
            if read[ctr]=="1":
                commonList[ctr]+=1
    #print(commonList)
    for ctr2 in range(len(commonList)):
        oneCount = commonList[ctr2]
        zeroCount = len(base) - oneCount
        if oneCount>zeroCount:
            mostCommonBinList[ctr2] = 1
        elif oneCount == zeroCount:
            mostCommonBinList[ctr2] = 1
        else: 
            mostCommonBinList[ctr2] = 0
    return mostCommonBinList

def getMostCommonCO(base):
    commonList = [0,0,0,0,0,0,0,0,0,0,0,0]
    mostCommonBinList = [0,0,0,0,0,0,0,0,0,0,0,0]
    for read in base:
        for ctr in range(len(read)):
            if read[ctr]=="1":
                commonList[ctr]+=1
    #print(commonList)
    for ctr2 in range(len(commonList)):
        oneCount = commonList[ctr2]
        zeroCount = len(base) - oneCount
        if oneCount>zeroCount:
            mostCommonBinList[ctr2] = 0
        elif oneCount == zeroCount:
            mostCommonBinList[ctr2] = 0
        else: 
            mostCommonBinList[ctr2] = 1
    return mostCommonBinList





def bitCriteriaOxygen(baseList, mostCommonList):
    segregatedList=[]
    presearch = ""
    
    
    for com in range(12):
        rev = 12 - com -1
        presearch += str(mostCommonList[com])
        searchLine = presearch+"\d{"+str(rev)+"}"
        #print(searchLine)
        for seg in baseList:
            if re.search(searchLine, seg):
                segregatedList.append(seg.split("\n")[0])
        #print("seg length: "+str(len(segregatedList)))
        #print(segregatedList)
        if len(segregatedList)<2:
            return segregatedList[0]
            
        
        baseList = segregatedList
        mostCommonList = getMostCommonOxy(segregatedList)
        #print(mostCommonList)
        segregatedList = []    
    #it should never reach here
    return "none"






def bitCriteriaCOScrub(baseList, mostCommonList):
    print(mostCommonList)
    segregatedList=[]
    presearch = ""
    for com in range(12):
        rev = 12 - com -1
        presearch += str(mostCommonList[com])
        searchLine = presearch+"\d{"+str(rev)+"}"
        #print(searchLine)
        for seg in baseList:
            if re.search(searchLine, seg):
                segregatedList.append(seg.split("\n")[0])
        #print("seg length: "+str(len(segregatedList)))
        #print(segregatedList)
        if len(segregatedList)<2:
            
            return segregatedList[0]
            
        
        baseList = segregatedList
        mostCommonList = getMostCommonCO(segregatedList)
        #print(mostCommonList)
        segregatedList = []    
    #it should never reach here
    return "none"
    


f = open("input.txt")
readed = f.readlines()



mostCommonBin = getMostCommonOxy(readed)
binOxy = bitCriteriaOxygen(readed, mostCommonBin)

mostCommonBin = getMostCommonCO(readed)
binCO = bitCriteriaCOScrub(readed, mostCommonBin)
print("Binary Oxygen: "+binOxy)
print("Binary CO2: "+binCO)

oxy = stringBinaryToInt(binOxy)
co = stringBinaryToInt(binCO)

print("Oxygen: "+str(oxy))
print("CO2: "+str(co))

print(oxy*co)
