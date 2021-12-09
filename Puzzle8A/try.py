
f = open("input.txt")
readed = f.readlines()

numCode = [
    "abcefg",   #0
    "cf",       #1
    "acdeg",    #2
    "acdfg",    #3
    "bcdf",     #4
    "abdfg",    #5
    "abdefg",   #6
    "acf",      #7
    "abcdefg",  #8
    "abcdfg"    #9
]

numLenLookup ={
    "2":"1",
    "3":"7",
    "4":"4",
    "5":"235",
    "6":"069",
    "7":"8"
}

quickCount = {
    "0":0,
    "1":0,
    "2":0,
    "3":0,
    "4":0,
    "5":0,
    "6":0,
    "7":0,
    "8":0,
    "9":0
}

firstLine = readed[0]
#print(firstLine)


for read in readed:
    lineParser = read.split(" | ")
    unique = lineParser[0].split(" ")
    output = lineParser[1].split(" ")
    for out in output:
        #print(out)
        noReturn = out.split("\n")
        lenGet = len(noReturn[0])
        #print(lenGet)
        backToStr = str(lenGet)
        #print(backToStr)
        lenLookup = numLenLookup[backToStr]
        if len(lenLookup) == 1:
            quickCount[lenLookup] += 1
print(quickCount)

total1478 = quickCount["1"]+quickCount["4"]+quickCount["7"]+quickCount["8"]
print("final count: "+str(total1478))
