

import math

from constant import FALSE

f = open("input0.txt")
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
    1,
    2,
    3,
    4
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

def CompleteLine(strList):
    closerList = []
    for elem in strList:
        openPosition = openCharacters.index(elem[1])
        closerElem = closeCharacters[openPosition]
        closeState = CheckIfOpeningOrClose(closerElem)
        closerList.insert(0, closeState)
    return closerList

def GetMiddleScore(sList):
    print("target list length: "+str(len(sList)))
    middlePosi = len(sList)-(len(sList)/2)-1
    print("mid posi: "+str(middlePosi))
    
    print(sList[middlePosi])
    topCheck = False
    botCheck = False
    topEqualCheck = False
    botEqualCheck = False

    #lets check the upper and middle
    doWhile = True
    while doWhile:
        try:    
            topCheck = sList[middlePosi-1] < sList[middlePosi]
            topEqualCheck = sList[middlePosi-1] == sList[middlePosi]
        except:
            topCheck = True
            topEqualCheck = True
        try:
            botCheck = sList[middlePosi+1] > sList[middlePosi]
            botEqualCheck = sList[middlePosi+1] == sList[middlePosi]
        except:
            botCheck = True
            botEqualCheck = True
        
        print("is top "+str(sList[middlePosi-1])+" lower than "+str(sList[middlePosi])+" : "+str(topCheck))
        print("is top "+str(sList[middlePosi+1])+" higher than "+str(sList[middlePosi])+" : "+str(botCheck))

        if topCheck and botCheck:
            return middlePosi
        
        if topCheck == False and botCheck == True:
            if topEqualCheck:
                return middlePosi
            else:
                print("move left")
                middlePosi -= 1
                continue
        
        if topCheck == True and botCheck == False:
            if botEqualCheck:
                return middlePosi
            else:
                print("move right")
                middlePosi += 1
                continue
        
        #if topCheck == False and botCheck == False:
        #    if topEqualCheck == False and botEqualCheck == False:
                #its fubarred lets just run down the length of the array and check for equality

        
          





    return middlePosi
    


# cleanIt
cleaned = []
for read in readed:
    cleaned.append(read.split("\n")[0])


#MAIN CODE
"""
resultList = []
incompleteList = []
lineScoreList = []
for clean in cleaned:
    resultList.append(ErrorCheckLine(clean))
for result in resultList:    
    if result[0] == "incomplete":
        incompleteList.append([clean, result[1]])
for inc in incompleteList:
    lineScore = 0
    completeIt = CompleteLine(inc[1])
    for elem in completeIt:
        getScore = scoreLookup[closeCharacters.index(elem[1])]
        lineScore = lineScore * 5 + getScore
    lineScoreList.append(lineScore)
lineScoreList.sort()
print(lineScoreList)
#find the middle score

"""



tryList1 = [2,3,4,5,6,7,8]
tryList2 = [2,3,4,4,5,6,7]
tryList3 = [2,3,4,5,5,6,7]
tryList4 = [2,3,5,5,5,6,7]


print(GetMiddleScore(tryList4))

