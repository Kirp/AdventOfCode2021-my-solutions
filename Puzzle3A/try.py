


def stringBinaryToInt(strb):
    toOut = 0
    size = len(strb)
    for ctr in range(size):
        rev = size - ctr -1
        toOut += int(strb[ctr]) * pow(2,rev)
    return toOut


f = open("input.txt")
readed = f.readlines()

commonList = [0,0,0,0,0,0,0,0,0,0,0,0]
gamma = ""
epsilon = ""

for read in readed:
    for ctr in range(len(read)):
        if read[ctr]=="1":
            commonList[ctr]+=1

print(commonList)

for ctr in range(len(commonList)):
    oneCount = commonList[ctr]
    zeroCount = 1000 - oneCount
    if oneCount>zeroCount:
        print("the most common in range "+str(ctr)+" is 1")
        gamma += "1"
        epsilon += "0"
    else: 
        print("the most common in range "+str(ctr)+" is 0")
        gamma += "0"
        epsilon += "1"

print("gamma: "+gamma)
print("epsilon: "+epsilon)
answer = stringBinaryToInt(gamma) * stringBinaryToInt(epsilon)
print(answer)





