f = open("subInput.txt")
readed = f.readlines()

frontMeasure = int(readed[0])
midMeasure = int(readed[0])+int(readed[1])
lastMeasure = int(readed[0])+int(readed[1])+int(readed[2])
depth = 0

for x in range(3, len(readed)):
    curNum = int(readed[x])
    #print(curNum)
    frontMeasure += curNum
    midMeasure += curNum
    if midMeasure > lastMeasure:
        depth +=1
    lastMeasure = midMeasure
    midMeasure = frontMeasure
    frontMeasure = curNum
print(depth)