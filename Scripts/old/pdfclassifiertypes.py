import glob
import os
import PyPDF2
from collections import Counter
import re
import slate3k as slate
import xlsxwriter

#WORDS TO SEARCH FOR

algo={'SVM':['SVM'],'PCA':['PC1','PC2'],'Neural':['ANN','RNN','CNN','Bayesian'],\
      'RL':['DQN','C51','SAC','DDPG','PPO','A2C','A3C','AlphaZero'],\
      'HMM':['Ergodic','Bakis','Left-Right','Bakis']}

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
    x=1
    res=0
    for k,v in algo.items():

        worksheet.write(xlsxwriter.utility.xl_col_to_name(0) + str(1), 'Title')
        worksheet.write(xlsxwriter.utility.xl_col_to_name(0)+str(i),key)
        for item in v:
            worksheet.write(xlsxwriter.utility.xl_col_to_name(x)+str(1),k+'-'+item)
            worksheet.write(xlsxwriter.utility.xl_col_to_name(x)+str(i), Counts[item]+Counts[item.upper()] + Counts[item+"s"]+Counts[item+"S"]+Counts[item.lower()]+Counts[item.lower()+"s"]+Counts[item.lower()+"S"])
            x+=1

workbook.close()



