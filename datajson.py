import glob
import os
import PyPDF2
import json
import re
import slate3k as slate
from requests_html import HTMLSession
import requests
from doi2bib import doi2bib

def datajson(path,Papers,url):
    for filename in glob.glob(os.path.join(path, '*.pdf')):
        Filename=filename.replace("C:\\Users\\prav\\PycharmProjects\\SVM\\PaperClassifier\\Papers\\", '')
        Filename = Filename.replace(".pdf", '')
        if Filename not in Papers:
            print (Filename)
            try:
                session = HTMLSession()
                r = session.get(url+Filename[1:])
                doi = r.html.search('"doi":"{}"')[0]
                return doi

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
