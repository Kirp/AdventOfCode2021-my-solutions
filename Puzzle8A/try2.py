
numCode = [
    "abcefg",   #0
    "cf",       #1
    "acdeg",    #2
    "acdfg",    #3
    "bcdf",     #4
    "abdfg",    #5
    "abdefg",   #6
    "acf",      #7
    "abcdefg",  #8
    "abcdfg"    #9
]



numLenLookup ={
    "2":"1",
    "3":"7",
    "4":"4",
    "5":"235",
    "6":"069",
    "7":"8"
}

quickCount = {
    "0":0,
    "1":0,
    "2":0,
    "3":0,
    "4":0,
    "5":0,
    "6":0,
    "7":0,
    "8":0,
    "9":0
}

standardSet = {
    "a":"a",
    "b":"b",
    "c":"c",
    "d":"d",
    "e":"e",
    "f":"f",
    "g":"g"
}

decoderSet = {
    "a":[],
    "b":[],
    "c":[],
    "d":[],
    "e":[],
    "f":[],
    "g":[]
}

def CountIndividualElementsInListReturnDictionary(list):
    #print("recieved")
    #print(list)
    outDict = {}
    for elem in list:
        keyList = outDict.keys()
        if keyList.count(elem) == 0:
            outDict[elem] = list.count(elem)
    #print("counted")
    #print(outDict)
    return outDict

def CheckIfUnequalAndAssignDominantValue(target):
    countIt = CountIndividualElementsInListReturnDictionary(target)
    print(countIt)
    targetSum = len(countIt)
    countSum = 0
    checker = 0
    highestElem = ""
    for countElem in countIt:
        countSum+=countIt[countElem]
        if countIt[countElem]>checker:
            checker = countIt[countElem]
            highestElem = countElem
    print("targetsum: "+str(targetSum))
    print("countsum: "+ str(countSum))
    if targetSum == countSum:
        print("skip it")
        return target
    else:
        print("unequality wow")
        
        return [highestElem]
        
        
        

def SumAndCompressCodeDict(original):
    sorted = {}
    unsorted = original.copy()

    #while len(unsorted)>0:
    #get the sorted
    for set in original:
        if len(original[set]) == 1:
            #pass it to sorted
            sorted[set] = original[set]
            unsorted.pop(set)
        else:
            #lets see if we can compress it
            unset = original[set]

            tempCounter = unset
            #tempCounter = CheckIfUnequalAndAssignDominantValue(unset)
            print(tempCounter)
            unsorted[set] = tempCounter
    
    print("sorted and unsorted")
    print(sorted)
    print(unsorted)
    original = unsorted.copy()

    return sorted
    
    

def GrokTheSet(uniq, set):
    decoderLenCheck = [2,3,4,7]
    codeDict = decoderSet.copy()
    for decode in decoderLenCheck:
        for item in uniq:
            #remove those nasty carriage returns
            item = item.split("\n")[0]
            if decode == len(item):
                print("found a decodable : "+item)
                codeNum = int(numLenLookup[str(decode)])
                front = numCode[codeNum]
                #print("decode with : "+front)
                for letCtr in range(len(front)):
                    #print("swap "+ front[letCtr]+ " with "+ item[letCtr])
                    #set[front[letCtr]] = item[letCtr]
                    #add in the codeLookup
                    codeDict[front[letCtr]].append(item[letCtr])

    print(codeDict)
    summed = SumAndCompressCodeDict(codeDict)

    finalOut = {}
    #flip it
    for item in summed:
        finalOut[summed[item][0]] = item

    #print(finalOut)
    return finalOut


def DecodeBrokenSignal(signal):
    decodedSet = standardSet.copy()
    lineParser = signal.split(" | ")
    unique = lineParser[0].split(" ")
    output = lineParser[1].split(" ")
    decodedSet = GrokTheSet(unique, decodedSet)
    pass
    """
    for out in output:
        out = out.split("\n")[0]
        decoded = ""
        print("decode : "+out)
        for octr in range(len(out)):
            decoded += decodedSet[out[octr]]
        print("decoded: "+decoded)
    """
    




f = open("inpu.txt")
readed = f.readlines()


firstLine = readed[0]
#print(firstLine)
print(DecodeBrokenSignal(firstLine))


   

#total1478 = quickCount["1"]+quickCount["4"]+quickCount["7"]+quickCount["8"]
#print("final count: "+str(total1478))
