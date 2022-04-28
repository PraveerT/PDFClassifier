import xlsxwriter
import json
from datajson import datajson
from Counter import countword
from counterregex import finder
from pathlib import Path
import os


url = 'https://ieeexplore.ieee.org/document/'
path = "C:\\Users\\prav\\PycharmProjects\\SVM\\PaperClassifier\\Papers\\"

Ofile='Gesture_recognition_paper'

a='Clustering'
b='Partitional'
cell_content = ['IEEEID', 'Bibtex']

algo = {}


try:
    f = open('data\\'+Ofile+'.json', )
    Papers = json.load(f)


except:
    Papers = {}
    Paperjson = json.dumps(Papers)
    f = open('data\\'+Ofile+'.json', "w")
    f.write(Paperjson)
    f.close()



paperName=[]


datajson(path,Papers,url,Ofile)

word={}


bib = open("bib.txt", "w")


ranking={}

str_path='file:///C:/Users/prav/PycharmProjects/SVM/PaperClassifier/Papers/'
for key,value in Papers.items():
    path = (str_path+key+'.pdf')
    Counts = finder(a,b,str(Papers[key]))
    word[str(value)] = Counts,path,value[2],path
    bib.write(value[1] + "\n")


for k,v in word.items():

    print (v[0],v[2],v[3])







