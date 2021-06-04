import glob
import os
import PyPDF2
from collections import Counter
import re
import slate3k as slate
import xlsxwriter
import datetime
import requests
import json
from requests_html import HTMLSession
import re
import operator

#output classifier file name

x='EM'

Ofile='Gesture_recognition_paper'


# algo={'SVM':['SVM'],'PCA':['PC1','PC2','PCA'],'Neural':['ANN','RNN','CNN','Bayesian','DNN'],\
#       'RL':['DQN','C51','SAC','DDPG','PPO','A2C','A3C','AlphaZero','RL'],\
#       'HMM':['Ergodic','Bakis','Left-Right','Bakis','HMM'],'ADS':['ADS'],'BIRCH':['BIRCH'],\
#       'CDBN':['CDBN'],'DBN':['DBN'],'EM':['EM'],'GTM':['GTM'],'ICA':['ICA'],'MARL':['MARL'],'MLP':['MLP'],\
#       'MRL':['MRL'],'MDS':['MDS'],'NMF':['NMF'],'NMDS':['NMDS'],'RBM':['RBM'],'SON':['SON'],'SSAE':['SSAE'],\
#       't-SNE':['t-SNE'],'WSN':['WSN'],'MCA':['MCA'],'LLE':['LLE'],'LRD':['LRD'],\
#       'vehicles':['car','bus','truck','bike','skateboard'],\
#       'body':['hand','body','face','arm','leg','finger'],'body':['hand','body','face','arm','leg','finger','head'],\
#       'type':['camera','radar','optical','mm-wave','Millimeter','mm','5G','4G','6G']}
algo={x:[x],'hand':['hand'],'body':['body'],'face':['face','head']}
try:
    f = open('data\\'+Ofile+'.json', )
    Papers = json.load(f)


except:
    Papers = {}
    Paperjson = json.dumps(Papers)
    f = open('data\\'+Ofile+'.json', "w")
    f.write(Paperjson)
    f.close()


def doi2bib(cite):
  url = "http://dx.doi.org/" + doi

  headers = {"accept": "application/x-bibtex"}
  re = requests.get(url, headers = headers)
  return re.text


url = 'https://ieeexplore.ieee.org/document/'

paperName=[]
path = "C:\\Users\\prav\\PycharmProjects\\SVM\\PaperClassifier\\Papers\\"

for filename in glob.glob(os.path.join(path, '*.pdf')):
    Filename=filename.replace("C:\\Users\\prav\\PycharmProjects\\SVM\\PaperClassifier\\Papers\\", '')
    Filename = Filename.replace(".pdf", '')
    if Filename not in Papers:
        print (Filename)
        try:
            session = HTMLSession()
            r = session.get(url+Filename[1:])
            doi = r.html.search('"doi":"{}"')[0]

        except requests.exceptions.RequestException as e:
            print(e)

        try:
            FN=PyPDF2.PdfFileReader(filename).getDocumentInfo()['/Title']


        except:
            FN=filename

        with open(filename, 'rb') as f:
            cite = re.search('{(.*?),',(doi2bib(doi))).group(1)
            extracted_text = slate.PDF(f)
            DOI=doi2bib(doi)

            Papers[str(Filename)]=extracted_text,DOI,'\cite{'+cite+'}'

Paperjson = json.dumps(Papers)
f = open('data\\'+Ofile+'.json',"w")
f.write(Paperjson)
f.close()

i=1
word={}
workbook = xlsxwriter.Workbook('Classification_sheets\\'+ x + '.xlsx')
worksheet = workbook.add_worksheet()
cell_format = workbook.add_format({'bold': True})
worksheet.write(xlsxwriter.utility.xl_col_to_name(0) + str(1), 'IEEEID')
worksheet.write(xlsxwriter.utility.xl_col_to_name(1) + str(1), 'Bibtex')
worksheet.write(xlsxwriter.utility.xl_col_to_name(7) + str(1), str(x)+' '+'hand')
worksheet.write(xlsxwriter.utility.xl_col_to_name(8) + str(1), str(x)+' '+'body')
worksheet.write(xlsxwriter.utility.xl_col_to_name(9) + str(1), str(x)+' '+'head/face')
bib = open("bib.txt", "w")
for key,value in Papers.items():

    PaperWordList=[]
    WordList = re.sub("[^\w]", " ",str(Papers[key])).split()
    PaperWordList.append(WordList)
    PaperWordList = [item for sublist in PaperWordList for item in sublist]
    Counts =Counter(PaperWordList)
    StrCounts=str(Counts)


    i += 1
    letnum=1
    x=2
    res=0
    bib.write(value[1] + "\n")
    for k,v in algo.items():


        worksheet.write(xlsxwriter.utility.xl_col_to_name(0)+str(i),key)
        worksheet.write(xlsxwriter.utility.xl_col_to_name(1)+str(i),value[2])
        for item in v:
            Spec_word_count=Counts[item] + Counts[item.upper()] \
            + Counts[item + "s"] + Counts[item + "S"] + Counts[item.lower()] + Counts[item.lower() + "s"] \
            + Counts[item.lower() + "S"] + Counts[item.capitalize()]
            word[str(v)]=Spec_word_count,k


            worksheet.write(xlsxwriter.utility.xl_col_to_name(x)+str(1),k+'-'+item)
            worksheet.write(xlsxwriter.utility.xl_col_to_name(x)+str(i),Spec_word_count)
            x+=1

        # worksheet.write(xlsxwriter.utility.xl_col_to_name(x) + str(1), 'Body')
        # worksheet.write(xlsxwriter.utility.xl_col_to_name(x+1) + str(1), 'Algo')
        # worksheet.write(xlsxwriter.utility.xl_col_to_name(x + 2) + str(1), 'Type')
        worksheet.write_formula(xlsxwriter.utility.xl_col_to_name(x) + str(i),'=IF(AND(C'+str(i)+'>10,D'+str(i)+'>10),B'+str(i)+',"")')
        worksheet.write_formula(xlsxwriter.utility.xl_col_to_name(x+1) + str(i),'=IF(AND(C'+str(i)+'>10,E'+str(i)+'>10),B'+str(i)+',"")')
        worksheet.write_formula(xlsxwriter.utility.xl_col_to_name(x+2) + str(i),'=IF(OR(AND(C'+str(i)+'>10,F'+str(i)+'>10),AND(C'+str(i)+'>10,F'+str(i)+'>10)),B'+str(i)+',"")')

        # worksheet.write_formula(xlsxwriter.utility.xl_col_to_name(x) + str(i),'=INDEX($AZ$1:$BF$1,1,MATCH((LARGE(AZ'+str(i)+':BF'+str(i)+',1)),AZ'+str(i)+':BF'+str(i)+',0))')
        # worksheet.write_formula(xlsxwriter.utility.xl_col_to_name(x+1) + str(i),'=INDEX($C$1:$AT$1,1,MATCH(LARGE(C'+str(i)+':AT'+str(i)+',1),C'+str(i)+':AT'+str(i)+',0))')
        # worksheet.write_formula(xlsxwriter.utility.xl_col_to_name(x+2) + str(i),'=INDEX($BF$1:$BN$1,1,MATCH(LARGE(BF'+str(i)+':BN'+str(i)+',1),BF'+str(i)+':BN'+str(i)+',0))')
        # worksheet.write_formula(xlsxwriter.utility.xl_col_to_name(x+3) + str(i),'=IF(AND(BQ'+str(i)+'=$C$1,BP'+str(i)+'=$AZ$1),B'+str(i)+',"")')


        worksheet.set_row(i-1, 20)

worksheet.freeze_panes(1, 0)
workbook.close()
#
# from tabulate import tabulate
# table = [["spam",42],["eggs",451],["bacon",0]]
# headers = ["item", "qty"]
#
# print (tabulate(table,headers, tablefmt="latex_raw"))