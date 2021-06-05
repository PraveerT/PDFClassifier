
import xlsxwriter

import json

from datajson import datajson
from Counter import countword


#output classifier file name

x='EM'
url = 'https://ieeexplore.ieee.org/document/'
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



paperName=[]
path = "C:\\Users\\prav\\PycharmProjects\\SVM\\PaperClassifier\\Papers\\"

datajson(path,Papers,url)

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
    Counts=countword(Papers,key,value)


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

        worksheet.write_formula(xlsxwriter.utility.xl_col_to_name(x) + str(i),'=IF(AND(C'+str(i)+'>10,D'+str(i)+'>10),B'+str(i)+',"")')
        worksheet.write_formula(xlsxwriter.utility.xl_col_to_name(x+1) + str(i),'=IF(AND(C'+str(i)+'>10,E'+str(i)+'>10),B'+str(i)+',"")')
        worksheet.write_formula(xlsxwriter.utility.xl_col_to_name(x+2) + str(i),'=IF(OR(AND(C'+str(i)+'>10,F'+str(i)+'>10),AND(C'+str(i)+'>10,F'+str(i)+'>10)),B'+str(i)+',"")')



        worksheet.set_row(i-1, 20)

worksheet.freeze_panes(1, 0)
workbook.close()
