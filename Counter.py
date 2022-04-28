import re
from collections import Counter
def countword(Papers,key,value):


    PaperWordList=[]
    WordList = re.findall(r"[\w']+",str(Papers[key]))
    WordList2=re.findall(r"[\w']+"+" "r"[\w']+",str(Papers[key]))
    WordList3 = re.findall(r"[\w']+" + " "r"[\w']+"+ " "r"[\w']+", str(Papers[key]))
    PaperWordList.append(WordList)
    PaperWordList.append(WordList2)
    PaperWordList.append(WordList3)
    PaperWordList = [item for sublist in PaperWordList for item in sublist]
    Counts =Counter(PaperWordList)
    StrCounts=str(Counts)
    print (Counts)
    return Counts