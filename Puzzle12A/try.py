


class Nodes:
    def __init__(self, name, connection):
        self.name = name
        self.connections =[]
        self.connections.append(connection)
    
    def AddConnections(self, newConnection):
        self.connections.append(newConnection)


#--
f = open("input0.txt")
readed = f.readlines()

cleaned = []
for read in readed:
    cleaned.append(read.split("\n")[0])
#--

#Main starts here
nodeList = {}
for clean in cleaned:
    dataSplit = clean.split("-")
    try:
        nodeList[dataSplit[0]].append(dataSplit[1])
    except:
        nodeList[dataSplit[0]] = [dataSplit[1]]
    #and reverse
    try:
        nodeList[dataSplit[1]].append(dataSplit[0])
    except:
        nodeList[dataSplit[1]] = [dataSplit[0]]
    

print(str(len(nodeList)))
for node in nodeList:
    print(node)
    print(nodeList[node])