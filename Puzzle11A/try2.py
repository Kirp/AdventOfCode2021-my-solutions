 

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
            #if ctrx != 0 and ctry !=0:
            tempx = x+ctrx
            tempy = y+ctry
            if tempx < 0 or tempx >= wid:
                continue
            if tempy < 0 or tempy >= hei:
                continue
            namer = str(tempx)+"x"+str(tempy)
            if dict[namer] != 0:
                dict[namer] +=1
            
    return dict

def GetGlowUps(wid, hei, dict):
    glow = []
    for y in range(hei):
        for x in range(wid):
            namer = str(x)+"x"+str(y)
            if dict[namer] > 9:
                #dict[namer] = 0
                glow.append(namer)
    #print(glow)   
    return glow

def GlowExplodeAndSpendEnergy(wid, hei, glowList, dict):
    explodeCount = 0
    for glow in glowList:
        if dict[glow] > 9:
            dict[glow] = 0
            explodeCount +=1
            coord =  glow.split("x")
            dict = RaisePowerAdjacent(int(coord[0]),int(coord[1]), wid, hei, dict)
    return [dict, explodeCount]

            
def OctoEnergyUp(wid, hei, dict):
    glowUpList = []
    for y in range(wid):
        for x in range(hei):
            namer = str(x)+"x"+str(y)
            dict[namer]+=1
    
    glowLoop = True
    boomCount = 0
    while glowLoop==True:
        seek = GetGlowUps(wid,hei,dict)
        #DisplayOctoMatrix(wid, hei, dict)
        glowUpList = seek
        seek = GlowExplodeAndSpendEnergy(wid, hei, glowUpList, dict)
        dict = seek[0]
        boomCount += seek[1]
        lastCheck = GetGlowUps(wid, hei, dict)
        if len(lastCheck) == 0:
            glowLoop = False



    #DisplayOctoMatrix(wid, hei, dict)
    return [dict, boomCount]
    
#clean it
cleaned = []
for read in readed:
    cleaned.append(read.split("\n")[0])



#load it in a dictionary
octoWidth = len(cleaned[0])
octoHeight = len(cleaned)
octoMatrix = {}
for y in range(octoHeight):
    for x in range(octoWidth):
        namer = str(x)+"x"+str(y)
        octoMatrix[namer]= int(cleaned[y][x])

#totalBoomCount = 0
for count in range(500):

    feedback = OctoEnergyUp(octoWidth, octoHeight,octoMatrix)
    octoMatrix = feedback[0]
    print("booms in count "+str(count)+" : "+str(feedback[1]))
    if feedback[1] == 100:
        print("all octo flash!")
        break

DisplayOctoMatrix(octoWidth, octoHeight, octoMatrix)

#440 <- final answer
