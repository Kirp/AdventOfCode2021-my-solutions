import constant

f = open("input.txt")
readed = f.readlines()



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
    return [base, isLow]
    


#clean it up first
cleaned = []
for ctr in range(len(readed)):
    readed[ctr] = readed[ctr].split("\n")[0]

print("height: "+str(len(readed)))
print("width: " +str(len(readed[0])))



lowList = []
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
        if lowPoint[1] == constant.TRUE:
            #print("lowest at "+str(x)+"x"+str(y))
            #addToLowList
            lowList.append(lowPoint[0]+1)
finale = 0
for low in lowList:
    finale += low
print("final answer: "+str(finale))

