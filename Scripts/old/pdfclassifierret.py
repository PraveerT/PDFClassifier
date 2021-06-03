import glob
import os
import PyPDF2
from collections import Counter
import re



paper=[]
paperName=[]
path = "C:\\Users\\prav\\Downloads\\Machine learning papers"
for filename in glob.glob(os.path.join(path, '*.pdf')):
    print (PyPDF2.PdfFileReader(filename).getDocumentInfo())
    paper.append(PyPDF2.PdfFileReader(filename))

    Filename=filename.replace("C:\\Users\\prav\\Downloads\\Machine learning papers\\", '')
    paperName.append(Filename)






Papers={}
for x in range(0,len(paper)):
    pages={}
    NumPages=paper[x].getNumPages()

    for i in range(NumPages):
        pages[str(paperName[x])+"_"+ str(x+1)+"page_"+str(i+1)]=paper[x].getPage(i-1).extractText()
    Papers[str(paperName[x])]=pages
i=1
for keys,values in Papers.items():
    for k,v in values.items():
        PaperWordList=[]
        WordList = re.sub("[^\w]", " ",values[k]).split()
        PaperWordList.append(WordList)
        PaperWordList = [item for sublist in PaperWordList for item in sublist]
        #print(k)
        #print (v)
    Counts =Counter(PaperWordList)


    print('Linear ',Counts['Linear']+Counts['linear'],'Logistic ',Counts['logistic']+Counts['Logistic']\
          ,'Classification ',Counts['Classification']+Counts['classification']\
          ,'Regression ',Counts['Regression']+Counts['regression'] \
          , 'Naive ', Counts['Naive'] + Counts['naive'] \
          , 'K-Nearest ', Counts['K-Nearest'] + Counts['K-nearest']+ Counts['k-nearest'] +Counts['KNN']\
          , 'Learning Vector Quantization ', Counts['LVQ'] \
          , 'Support Vector Machines ', Counts['SVM']+Counts['SVMs']\
          , 'Learning Vector Quantization ', Counts['LVQ'] \
          , 'PCA ', Counts['PCA'] \
          ,'Forest', Counts['Forest']+Counts['forest']\
          , 'Neural', Counts['neural'] + Counts['ANN']+Counts['CNN']+Counts['RNN']+Counts['NN'])




