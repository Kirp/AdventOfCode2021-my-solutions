f = open("inp.txt")
readed = f.readlines()

#print(readed[0])

depth = 0
hori = 0

for read in readed:
    splitter = read.split(" ")
    #print(splitter)
    if splitter[0] == "forward":
        hori += int(splitter[1])
    if splitter[0] == "up":
        depth -= int(splitter[1])
    if splitter[0] == "down":
        depth += int(splitter[1])
print("Horizontal : "+str(hori))
print("Depth      : "+str(depth))
print("Final Answer : "+str(hori*depth))