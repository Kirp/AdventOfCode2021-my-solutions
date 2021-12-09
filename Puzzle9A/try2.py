from os import remove
import constant

f = open("input.txt")
readed = f.readlines()

def RemoveCopies(base, remove):
    acopy = remove
    toRemove = []
    for ctr in range(len(acopy)):
        acop = acopy[ctr]
        if base[0] == acop[0] and base[1] == acop[1]:
            toRemove.append(ctr)
    toRemove.reverse()
    for rem in toRemove:
        remove.pop(rem)
    return remove

def RemoveDoubles(removeList):
    copyList = removeList
    delList = []
    for copoo in copyList:
        doubleCount = 0
        for remCtr in range(len(removeList)):
            rem = removeList[remCtr]
            if copoo[0] == rem[0] and copoo[1] == rem[1]:
                if doubleCount<1:
                    doubleCount+=1
                else:
                    if delList.count(remCtr) == 0:
                        delList.append(remCtr)
    #print("del list")
    #print(delList)
    delList.sort()
    delList.reverse()
    for elem in delList:
        removeList.pop(elem)
    return removeList
    

def GetSurroundingCellsWithExactValue(x,y,value):
    pass

def IsInListCheck(check, inList):
    for lister  in inList:
        if check[0]==lister[0] and check[1]==lister[1]:
            return constant.TRUE
    return constant.FALSE

def GetSurroundingCellsHigherValue(x,y, value):
    hardUpperLimit = 9
    surround = []
    testValue = 0
    if y >0:
        testValue = int(readed[y-1][x])
        if testValue > value and testValue < hardUpperLimit:
            surround.append([x,y-1,testValue])
    if y < len(readed)-1:
        testValue = int(readed[y+1][x])
        if testValue > value and testValue < hardUpperLimit:
            surround.append([x,y+1,testValue])
    if x > 0:
        testValue = int(readed[y][x-1])
        if testValue > value and testValue < hardUpperLimit:
            surround.append([x-1,y,testValue])
    if x < len(readed[0])-1:
        testValue = int(readed[y][x+1])
        if testValue > value and testValue < hardUpperLimit:
            surround.append([x+1,y,testValue])
    return surround

def GetBasinCells(x,y):
    unsorted = []
    sorted = []
    base = [x,y,int(readed[y][x])]
    sorted.append(base)
    #print("sorted")
    #print(sorted)
    if base[2]+1 <9:
        unsorted = GetSurroundingCellsHigherValue(base[0],base[1],base[2])
    else:
        return sorted
    
    #print("first unsort")
    #print(unsorted)

    while(len(unsorted)>0):
        newCells = []
        for un in unsorted:
            newCells += GetSurroundingCellsHigherValue(un[0],un[1], un[2])
        #newCells = RemoveDoubles(newCells)
        #print("new cells 1")
        #print(newCells)

        sorted += unsorted
        for sort in sorted:
            newCells = RemoveCopies(sort, newCells)    

        newCells = RemoveDoubles(newCells)
        
        #print("newcells 2")
        #print(newCells)
        #first remove all sorted copies in unsorted
        for sort in sorted:
            unsorted = RemoveCopies(sort, newCells)
        #print("2nd sorted")
        #print(sorted)
        #print("2nd unsorted")
        #print(unsorted)
    return sorted


def IsALowPoint(base, checkList):
    #print("base: "+str(base))
    #print("checkList:")
    #print(checkList)
    isLow = constant.TRUE
    for check in checkList:
        if check < 10:
            #print("test: "+str(check))
            if check <= base:
                #print("lower!")
                if isLow == constant.TRUE:
                    isLow = constant.FALSE
    #print("Is "+str(base)+" lowest? "+ str(isLow))
    return isLow
    


#clean it up first
cleaned = []
for ctr in range(len(readed)):
    readed[ctr] = readed[ctr].split("\n")[0]

print("height: "+str(len(readed)))
print("width: " +str(len(readed[0])))



basinList = []
for y in range(len(readed)):
    for x in range(len(readed[0])):
        top = 10
        bot = 10
        left = 10
        right = 10
        base = int(readed[y][x])
        if y >0:
            top = int(readed[y-1][x])
        if y < len(readed)-1:
            bot = int(readed[y+1][x])
        if x > 0:
            left = int(readed[y][x-1])
        if x < len(readed[0])-1:
            right = int(readed[y][x+1])
        
        lowPoint = IsALowPoint(base, [top, left, right, bot])
        #print("result if lowest: "+str(lowPoint[1]))
        if lowPoint == constant.TRUE:
            #print("lowest at "+str(x)+"x"+str(y))
            basinList.append(GetBasinCells(x,y))

sortable = []
for basin in basinList:
    sortable.append(len(basin))

sortable.sort()
sortable.reverse()
#print(sortable)
print("3 largest")
print(sortable[0])
print(sortable[1])
print(sortable[2])

final = sortable[0]*sortable[1]*sortable[2]
print("final answer: "+str(final))

"""            
tryIt = GetBasinCells(6,4)
print(len(tryIt))
"""



