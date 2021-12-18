
import constant

f = open("input.txt")
readed = f.readlines()


openCharacters = [
    "(",
    "[",
    "{",
    "<"
]

closeCharacters = [
    ")",
    "]",
    "}",
    ">"
]

scoreLookup = [
    3,
    57,
    1197,
    25137
]




def CheckIfOpeningOrClose(strElem):
    for open in openCharacters:
        if open == strElem:
            return ["open", strElem]
    for close in closeCharacters:
        if close == strElem:
            return ["close", strElem]
    return ["unlisted", strElem]

def ValidEntryCheck(listEntry, strList):
    if len(strList)==0:
        return ["validEnter"]
    
    lastValid = strList[len(strList)-1]
    if lastValid[0] == "open":
        #expect closed
        if listEntry[0] == "close":
            #compare if correct
            #print("compare "+str(lastValid[1])+" with "+str(listEntry[1]))
            openPosition = openCharacters.index(lastValid[1])
            if listEntry[1]==closeCharacters[openPosition]:
                return ["validPair"]
            else:

                return ["invalid",closeCharacters[openPosition],listEntry[1]]
        elif listEntry[0] == "open":
            return ["validEnter"]
    elif lastValid[0] == "close":
        return ["unexpected", lastValid[1]]
    
    return ["total failure"]

        
        


        


def ErrorCheckLine(strList):
    opCloList = []
    for elem in strList:
        elemState = CheckIfOpeningOrClose(elem)
        #print(elemState)
        opCloCheckResult = ValidEntryCheck(elemState, opCloList)
        #print("result")
        #print(opCloCheckResult)
        if opCloCheckResult[0] == "validEnter":
            opCloList.append(elemState)
        if opCloCheckResult[0] == "validPair":
            #just pop out the last value in the opCLoList
            opCloList.pop()
        if opCloCheckResult[0] == "invalid":
            return opCloCheckResult
    if len(opCloList)==0:
        return ["clear",opCloList]
    return ["incomplete",opCloList]
    

    


# cleanIt
cleaned = []
for read in readed:
    cleaned.append(read.split("\n")[0])


resultList = []
score = 0
for clean in cleaned:
    resultList.append(ErrorCheckLine(clean))
for result in resultList:
    if result[0] == "invalid":
        #print(result)
        getScore = scoreLookup[closeCharacters.index(result[2])]
        #print("error score: "+str(getScore))
        score += getScore
print("final score: "+str(score))

"""
tryIt = ErrorCheckLine(cleaned[1])
print(tryIt)
"""


