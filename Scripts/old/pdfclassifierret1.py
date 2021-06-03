import glob
import os
import PyPDF2
from collections import Counter
import re
import slate3k as slate
import xlsxwriter

#WORDS TO SEARCH FOR
wordlist=['Machine','SVM','K-mean','Linear','PCA','Forest','Neural','Naive'\
          ,'Bayesian','neural','ANN','RNN','CNN','Classification'\
          ,'LVQ','Logistic','Regression','DQN','Precision','K-L','Margin'\
          ,'Greedy','Beam','Quasi-Newton','Quadratic','Deep']


Letterlist=['A', 'B', 'C', 'D','E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','AA','AB']
Papers={}
paperName=[]
path = "C:\\Users\\prav\\Downloads\\ML"

for filename in glob.glob(os.path.join(path, '*.pdf')):
    print(filename)
    Filename=filename.replace("C:\\Users\\prav\\Downloads\\ML\\", '')
    try:
        FN=PyPDF2.PdfFileReader(filename).getDocumentInfo()['/Title']

    except:
        FN=Filename
    with open(filename, 'rb') as f:
        extracted_text = slate.PDF(f)
        Papers[str(FN)]=extracted_text

i=1
workbook = xlsxwriter.Workbook('PaperClassifier/classification.xlsx')
worksheet = workbook.add_worksheet()
for key,value in Papers.items():

    PaperWordList=[]
    WordList = re.sub("[^\w]", " ",str(Papers[key])).split()
    PaperWordList.append(WordList)
    PaperWordList = [item for sublist in PaperWordList for item in sublist]
    Counts =Counter(PaperWordList)
    StrCounts=str(Counts)
    i += 1
    letnum=1
    for word in wordlist:
        worksheet.write(Letterlist[0] + str(1), 'Title')
        worksheet.write(Letterlist[0]+str(i),key)
        worksheet.write(Letterlist[letnum]+str(1),word)
        worksheet.write(Letterlist[letnum]+str(i), Counts[word]+Counts[word.upper()] + Counts[word+"s"]+Counts[word+"S"]+Counts[word.lower()]+Counts[word.lower()+"s"]+Counts[word.lower()+"S"])
        letnum+=1
workbook.close()



