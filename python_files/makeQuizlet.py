def import_words(fname:str) -> list:
    vocab = []
    with open(fname, "r") as file:
        for line in file:
            line = line.strip()
            if line != "":
                word = line.split(";")
                vocab.append({"simplified": word[0], "meaning": word[1]})
    return vocab

from hanziconv import HanziConv
import pinyin
def add_to_list(vocab_list: list) -> list:
    toReturn = []
    for item in vocab_list:
        item["traditional"] = HanziConv.toTraditional(item["simplified"])
        item["pinyin"] = pinyin.get(item["simplified"])
        toReturn.append(item)
        
    return toReturn

def export_to_quizlet(fname: str, vocab_list: list) -> list:
    with open(fname, "w+") as file:
        for item in vocab_list:
            output = f"{item['simplified']}（{item['traditional']});{item['meaning']} ({item['pinyin']})\n"
            file.write(output)


word_list = import_words("hsk1/hsk1_vocab.txt")
word_list = add_to_list(word_list)
export_to_quizlet("quizOut/hsk1.txt",word_list)
