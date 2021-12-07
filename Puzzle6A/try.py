
f = open("input.txt")
readed = f.readlines()

fishList = []

for fish in readed[0].split(","):
    fishList.append(int(fish))

daysToSimulate = 80
for day in range(daysToSimulate):
    fishBirths = 0
    for ctr in range(len(fishList)):
        if fishList[ctr] == 0:
            fishList[ctr] = 6
            fishBirths+=1
        else:
            fishList[ctr]-=1
    for births in range(fishBirths):
        fishList.append(8)
    #print("after "+str(day)+" day")
    #print(fishList)
print(len(fishList))
