import xlsxwriter
import json
from datajson import datajson
from Counter import countword


url = 'https://ieeexplore.ieee.org/document/'
path = "C:\\Users\\prav\\PycharmProjects\\SVM\\PaperClassifier\\Papers\\"
Ofile='Gesture_recognition_paper'
#output classifier file name

interest=['HMM','SVM','RL','PCA','EM','ANN','RNN','Bayesian']
for m in interest:

    f = open("data\\algo.json")
    algo = json.load(f)
    algo[m]=[m]





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

    i=1
    word={}
    workbook = xlsxwriter.Workbook('Classification_sheets\\'+ m + '.xlsx')
    worksheet = workbook.add_worksheet()
    cell_format = workbook.add_format({'bold': True})
    worksheet.write(xlsxwriter.utility.xl_col_to_name(0) + str(1), 'IEEEID')
    worksheet.write(xlsxwriter.utility.xl_col_to_name(1) + str(1), 'Bibtex')
    worksheet.write(xlsxwriter.utility.xl_col_to_name(7) + str(1), (m)+' '+'hand')
    worksheet.write(xlsxwriter.utility.xl_col_to_name(8) + str(1), (m)+' '+'body')
    worksheet.write(xlsxwriter.utility.xl_col_to_name(9) + str(1), (m)+' '+'head/face')
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

            worksheet.write_formula(xlsxwriter.utility.xl_col_to_name(x) + str(i),'=IF(AND(G'+str(i)+'>10,C'+str(i)+'>10),B'+str(i)+',"")')
            worksheet.write_formula(xlsxwriter.utility.xl_col_to_name(x+1) + str(i),'=IF(AND(G'+str(i)+'>10,D'+str(i)+'>10),B'+str(i)+',"")')
            worksheet.write_formula(xlsxwriter.utility.xl_col_to_name(x+2) + str(i),'=IF(OR(AND(G'+str(i)+'>10,E'+str(i)+'>10),AND(G'+str(i)+'>10,E'+str(i)+'>10)),B'+str(i)+',"")')




            worksheet.set_row(i-1, 20)

    worksheet.freeze_panes(1, 0)
    workbook.close()
