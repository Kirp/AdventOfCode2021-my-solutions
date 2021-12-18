 

f = open("input0.txt")
readed = f.readlines()

def DisplayOctoMatrix(wid, hei,dict):
    for y in range(wid):
        displayList = ""
        for x in range(hei):
            namer = str(x)+"x"+str(y)
            displayList+=str(dict[namer])
        print(displayList)   
    print("\n")
    #print(displayList)
    pass    

def RaisePowerAdjacent(x,y, wid, hei, dict):
    for ctry in range(-1,2):
        for ctrx in range(-1,2):
            if ctrx != 0 and ctry !=0:
                tempx = x+ctrx
                tempy = y+ctry
                print("raise positioon: "+str(tempx)+"x"+str(tempy))
                """
                if tempx >0 or tempx< wid and tempy >0 or tempy < hei:
                    namer = str(tempx)+"x"+str(tempy)
                    print("position "+namer+ "with value "+str(dict[namer]))
                    if dict[namer] != 0:
                        dict[namer] +=1
                        print("position "+namer+ "with new value "+str(dict[namer]))
                """ 
    return dict

def GetGlowUps(wid, hei, dict):
    glow = []
    for y in range(hei):
        for x in range(wid):
            namer = str(x)+"x"+str(y)
            if dict[namer] > 9:
                print("position "+namer+ "glows up with value "+str(dict[namer]))
                dict[namer] = 0
                glow.append(namer)   
    return [dict, glow]

def GlowExplodeAndSpendEnergy(wid, hei, glowList, dict):
    for glow in glowList:
        if dict[glow] > 0:
            dict[glow] = 0
            coord =  glow.split("x")
            print(coord)
            dict = RaisePowerAdjacent(int(coord[0]),int(coord[1]), dict)
    seeker = GetGlowUps(wid, hei, dict)
    dict = seeker[0]
    glower = seeker[1]
    return [dict, glower]

                

    

def OctoEnergyUp(wid, hei, dict):
    
    glowUpList = []
    
    
    for y in range(wid):
        for x in range(hei):
            namer = str(x)+"x"+str(y)
            dict[namer]+=1
    seek = GetGlowUps(wid,hei,dict)
    print("glow up")
    print(seek[1])
    dict = seek[0]
    print("before glow up func")
    DisplayOctoMatrix(wid, hei, dict)
    glowUpList = seek[1]
    seek = GlowExplodeAndSpendEnergy(wid, hei, glowUpList, dict)
    dict = seek[0]
    glowUpList = seek[1]

    print("after glow up func")
    DisplayOctoMatrix(wid, hei, dict)
    return [dict, glowUpList]
    
#clean it
cleaned = []
for read in readed:
    cleaned.append(read.split("\n")[0])



#load it in a dictionary
octoWidth = len(cleaned[0])
octoHeight = len(cleaned)
print(octoWidth)
print(octoHeight)
octoMatrix = {}
for y in range(octoHeight):
    for x in range(octoWidth):
        namer = str(x)+"x"+str(y)
        octoMatrix[namer]= int(cleaned[y][x])

feedback = OctoEnergyUp(octoWidth, octoHeight,octoMatrix)
octoMatrix = feedback[0]
#print(octoMatrix)
#print(feedback)

print("run 2 \n")
feedback = OctoEnergyUp(octoWidth, octoHeight,octoMatrix)
octoMatrix = feedback[0]
#print(octoMatrix)
#print(feedback[1])
