import random as r
import sys

import googletrans as gt
from googletrans import Translator

def sentenceGame(fileArray):
    sentences = []
    for file in fileArray:
        for line in file:
            try:
                line = line.split(".",1)[1].strip("\n").strip()
                sentences.append(line)
            except:
                sentences.append(line)

    print("Possible Questions: " + str(len(sentences)))

    used = []
    for x in range(len(sentences)):
        used.append(0)
    count = 0
    while(input("Press enter to continue; q to quit: ") != "q"):
        
        usedVar = True
        x = 0
        while usedVar:
            x = r.randrange(0,len(sentences))
            if used[x] == 0:
                usedVar = False
                used[x] = 1

        print("\n" + sentences[x] + "\n")
       
        usedSum = 0
        for x in used:
            usedSum = usedSum + x

        if usedSum == 134:
            used = []
            for x in range(len(sentences)):
                used.append(0)
                
        count += 1
        print("Sentences Reviewed: " + str(count))


def outputSentences(fileArray,fileOut):
    sentences = []
    for file in fileArray:
        for line in file:
            try:
                line = line.split(".",1)[1].strip("\n").strip()
                sentences.append(line)
            except:
                sentences.append(line)

            
    count = 0
    trans = Translator()
    print("Please Wait :)")
    for sentence in sentences:
        sen = sentence.strip()
        translation = trans.translate(sen, src = "zh-cn")
        #print(translation)
        fileOut.write( sen +"\\" + translation.text + "\n")
        count += 1
    print("Lines Written: " + str(count))


if __name__ == "__main__":
    fileArray = []
    fileArray.append(open("chineseEnv/files/chinese/dictBank/finalReviewQuestions.txt","r"))
    fileOut = open("chineseEnv/files/chinese/quizOut/sentenceOutput.txt", "w")
 
    outputSentences(fileArray,fileOut) 
    
    for file in fileArray:
        file.close

    fileOut.close
    

    #try:
    #    sentenceGame(fileArray)
    #except:
    #    
    #    print("ERROR")

    #print("\n--- Game Over ---\n")