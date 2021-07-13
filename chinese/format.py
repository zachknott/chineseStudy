import random as r

def splitLine(line):
    initList = line.replace("\t"," ").replace("（"," (").rstrip("\n").split(" ",1)
    holder = initList[1]
    holder = holder.split("(")
    toList = []
    toList.append(initList[0])
    for item in holder:
        toList.append(item) 
    
    toReturn = []
    for piece in toList:
        charToRemove = "(）)"
        count = 0
        for charX in charToRemove:
            if count == 0:
                piece = piece.replace(charX, "")
                count += 1
            else:
                piece = piece.replace(charX, "")
        piece = piece.replace("\t"," ")
        piece = piece.strip()
        toReturn.append(piece)

    return toReturn

def formatCards(inFile,outFile):
    indexDictionary = []

    for line in inFile:
        brokenUp = splitLine(line)
        if len(brokenUp) < 3:
            print("Broke on Line" + str(brokenUp))
            print(len(brokenUp))
            continue

        indexDictionary.append(brokenUp)

    #r.shuffle(indexDictionary)

    count = 0
    for item in indexDictionary:
        outFile.write(str(indexDictionary[count][0]) + " " + str(indexDictionary[count][1]) + " (" + str(indexDictionary[count][2]) + ")\n")
        count += 1
        
    print("Num Cards Created: " + str(count))


if __name__ == "__main__":
    inFile = open("./dictBank/1thu5.txt","r")
    outFile = open("./quizOut/toUpload.txt", "a")

    formatCards(inFile, outFile)

    inFile.close
    outFile.close
