
f = open("subInput.txt")
readed = f.readlines()
lastMeasure = readed[0]
depth = 0

for x in readed:
    if int(x) > int(lastMeasure):
        depth +=1
    lastMeasure = x

print(depth)


