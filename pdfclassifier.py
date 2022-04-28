import xlsxwriter
import json
from datajson import datajson
from Counter import countword
from counterregex import finder

url = 'https://ieeexplore.ieee.org/document/'
path = "C:\\Users\\prav\\PycharmProjects\\SVM\\PaperClassifier\\Papers\\"

Ofile='Gesture_recognition_paper'

interest=['SVM','HMM','ANN','RNN','EM','RL','MLP','Bayesian','Neural']
compare_to={"geometry":["geometry"],"motion":["motion"]\
    ,"appearance":["appearance"],"space":["space"]}
cell_content = ['IEEEID', 'Bibtex']

algo = {}

for m in interest:

    algo.clear()
    algo.update(compare_to)

    algo[m]=[m]
    algokeys=list(algo.keys())




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
    workbook = xlsxwriter.Workbook('Classification_sheets\\'+ m + str(algokeys)+ '.xlsx')
    worksheet = workbook.add_worksheet()
    cell_format = workbook.add_format({'bold': True})

    for cellind in cell_content:
        worksheet.write(xlsxwriter.utility.xl_col_to_name(cell_content.index(cellind)) + str(1), str(cellind))
    bib = open("bib.txt", "w")


    ranking={}


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
                + Counts[item.lower() + "S"] + Counts[item.capitalize()] + Counts["n"+item]
                word[str(v)]=Spec_word_count,k



                worksheet.write(xlsxwriter.utility.xl_col_to_name(x)+str(1),k+'-'+item)
                worksheet.write(xlsxwriter.utility.xl_col_to_name(x)+str(i),Spec_word_count)
                x+=1

            ranking[item] = xlsxwriter.utility.xl_col_to_name(x-1)
        cellcounter=0
        for dictlen in range((len(algo))-1):

            worksheet.write(xlsxwriter.utility.xl_col_to_name(x + cellcounter) + str(1),(m+str(dictlen)))

            worksheet.write_formula(xlsxwriter.utility.xl_col_to_name(x+cellcounter) + str(i), \
                                    '=IF(AND(' + ranking[m] + str(i) + '>10,'+ xlsxwriter.utility.xl_col_to_name(dictlen+2) + str(i) + '>10),B' + str(i) + ',"")')
            cellcounter += 1
        worksheet.set_row(i-1, 20)


    worksheet.freeze_panes(1, 0)
    workbook.close()
