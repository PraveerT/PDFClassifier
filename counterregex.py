import re

import string

def finder(firstterm,secondterm,stringwords):

    resdict={}

    finda=re.sub('\s','  ',firstterm)
    findb = re.sub('\s', '  ', secondterm)
    stringwithspaces = re.sub('\s|^', '  ', stringwords)
    partialresult1=re.findall('\W'+finda+'\W|'+finda+'$|'+finda+' '\
                              '\W'+finda.lower()+'\W|'+finda.lower()+'$|'+finda.lower()+' '\
                              '\W'+finda.upper()+'\W|'+finda.upper()+'$|'+finda.upper()+' '\
                              '\W'+finda+'s'+'\W|'+finda+'s'+'$|'+finda+'s'+' '\
                              '\W'+finda+'S'+'\W|'+finda+'S'+'$|'+finda+'S'+' '\
                              '\W'+finda.capitalize()+'\W|'+finda.capitalize()+'$|'+finda.capitalize()+' ' \
                              '\W' +string.capwords(finda)+ '\W|' + string.capwords(finda) + '$|' + string.capwords(finda) + ' ' '$|' + string.capwords(finda) + ' '\
                              ,stringwithspaces)
    partialresult2=re.findall('\W'+findb+'\W|'+findb+'$|'+findb+' '\
                              '\W'+findb.lower()+'\W|'+findb.lower()+'$|'+findb.lower()+' '\
                              '\W'+findb.upper()+'\W|'+findb.upper()+'$|'+findb.upper()+' '\
                              '\W'+findb.capitalize()+'\W|'+findb.capitalize()+'$|'+findb.capitalize()+' ' \
                              '\W' +string.capwords(findb)+ '\W|' + string.capwords(findb) + '$|' + string.capwords(findb) + ' ' '$|' + string.capwords(findb) + ' '\
                              ,stringwithspaces)
    resdict[firstterm]=len(partialresult1)
    resdict[secondterm]=len(partialresult2)

    return resdict