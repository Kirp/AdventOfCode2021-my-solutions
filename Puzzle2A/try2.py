f = open("inp.txt")
readed = f.readlines()

#print(readed[0])

depth = 0
hori = 0
aim = 0

for read in readed:
    splitter = read.split(" ")
    if splitter[0] == "forward":
        hori += int(splitter[1])
        depth += aim * int(splitter[1])
    if splitter[0] == "up":
        aim -= int(splitter[1])
    if splitter[0] == "down":
        aim += int(splitter[1])
print("Horizontal : "+str(hori))
print("Aim : "+str(aim))
print("Depth : "+str(depth))
print("Final : "+str(depth*hori))
