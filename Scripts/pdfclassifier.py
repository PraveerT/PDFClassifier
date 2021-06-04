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
try:
    with open('data.json') as json_file:
        Papers = json.load(json_file)
except:
    Papers={}
    json = json.dumps(Papers)
    f = open("data.json", "w")
    f.write(json)
    f.close()




def doi2bib(cite):
  url = "http://dx.doi.org/" + doi

  headers = {"accept": "application/x-bibtex"}
  re = requests.get(url, headers = headers)
  return re.text


url = 'https://ieeexplore.ieee.org/document/'










algo={'SVM':['SVM'],'PCA':['PC1','PC2','PCA'],'Neural':['ANN','RNN','CNN','Bayesian','DNN'],\
      'RL':['DQN','C51','SAC','DDPG','PPO','A2C','A3C','AlphaZero','RL'],\
      'HMM':['Ergodic','Bakis','Left-Right','Bakis','HMM'],'ADS':['ADS'],'BIRCH':['BIRCH'],\
      'CDBN':['CDBN'],'DBN':['DBN'],'EM':['EM'],'GTM':['GTM'],'ICA':['ICA'],'MARL':['MARL'],'MLP':['MLP'],\
      'MRL':['MRL'],'MDS':['MDS'],'NMF':['NMF'],'NMDS':['NMDS'],'RBM':['RBM'],'SON':['SON'],'SSAE':['SSAE'],\
      't-SNE':['t-SNE'],'WSN':['WSN'],'MCA':['MCA'],'LLE':['LLE'],'LRD':['LRD'],\
      'vehicles':['car','bus','truck','bike','skateboard'],\
      'body':['hand','body','face','arm','leg','finger'],'body':['hand','body','face','arm','leg','finger'],\
      'type':['camera','radar','optical','mm-wave','Millimeter','mm','5G','4G','6G']}


paperName=[]
path = "C:\\Users\\prav\\Documents\\Papers"

for filename in glob.glob(os.path.join(path, '*.pdf')):
    Filename=filename.replace("C:\\Users\\prav\\Documents\\Papers\\", '')
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
            extracted_text = slate.PDF(f)
            Papers[str(Filename)]=extracted_text,doi2bib(doi)

json = json.dumps(Papers)
f = open("data.json","w")
f.write(json)
f.close()

i=1
workbook = xlsxwriter.Workbook('classification'+(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")+'.xlsx'))
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
    x=2
    res=0
    for k,v in algo.items():

        worksheet.write(xlsxwriter.utility.xl_col_to_name(0) + str(1), 'Title')
        worksheet.write(xlsxwriter.utility.xl_col_to_name(0)+str(i),key)
        worksheet.write(xlsxwriter.utility.xl_col_to_name(1)+str(i),value[1])
        for item in v:
            worksheet.write(xlsxwriter.utility.xl_col_to_name(x)+str(1),k+'-'+item)
            worksheet.write(xlsxwriter.utility.xl_col_to_name(x)+str(i), Counts[item]+Counts[item.upper()]\
                            + Counts[item+"s"]+Counts[item+"S"]+Counts[item.lower()]+Counts[item.lower()+"s"]\
                            +Counts[item.lower()+"S"]+Counts[item.capitalize()])
            x+=1

workbook.close()



