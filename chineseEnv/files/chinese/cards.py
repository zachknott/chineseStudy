import random as r
import time as t
    
def splitLine(line):
    toList = line.rstrip("\n").split(" ", 2)
    
    #print(toList)
    toReturn = []
    for piece in toList:
        charToRemove = "(（）)"
        count = 0
        for charX in charToRemove:
            if count == 0:
                piece = piece.replace(charX, "")
                count += 1
            else:
                piece = piece.replace(charX, "")
        toReturn.append(piece)

    return toReturn

def randoGen(indexDictionary):
    lenTest = 20
    randomList =[]
    for x in range(lenTest):
        #print(len(indexDictionary))
        randomList.append(r.randint(0,len(indexDictionary)-1))
        #print(randomList)

    charString = ""
    defString = ""
    pinString = ""

    for x in range(lenTest):
        charString = charString + indexDictionary[randomList[x]][0] + ""
        pinString = pinString + indexDictionary[randomList[x]][1] + " "
        defString = defString + indexDictionary[randomList[x]][2] + "; "
        

    print(charString + "\n")
    input("Press Enter to Continue")
    print(defString)


if __name__ == "__main__":



    #file = open("./dictBank/num.txt","r")
    file = open("./dictBank/dictionary.txt","r")

    indexDictionary = []

    for line in file:
        
        brokenUp = splitLine(line)
        if len(brokenUp) < 3:
            print("Broke on Line" + str(brokenUp))
            print(len(brokenUp))
            continue

        indexDictionary.append(brokenUp)

    randoGen(indexDictionary)
    
   