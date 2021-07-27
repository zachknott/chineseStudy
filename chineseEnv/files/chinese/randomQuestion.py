import random as r
from typing import Counter
import sys
sys.path.append('/usr/local/lib/python3.8/dist-packages')
from pypinyin import pinyin, lazy_pinyin, Style

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
        print(pinyin(sentences[x]))
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
    for sentence in sentences:
        fileOut.write(sentence.strip() +"\\" + "(answer)" + "\n")
        count += 1
    print("Lines Written: " + str(count))


if __name__ == "__main__":
    fileArray = []
    fileArray.append(open("chineseEnv/files/chinese/dictBank/finalReviewQuestions.txt","r"))
    fileOut = open("chineseEnv/files/chinese/quizOut/sentenceOutput.txt", "w")
 
    outputSentences(fileArray,fileOut) 
    
    

    #try:
    #    sentenceGame(fileArray)
    #except:
    #    
    #    print("ERROR")

    #print("\n--- Game Over ---\n")