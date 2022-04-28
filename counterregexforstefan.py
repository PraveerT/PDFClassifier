import re

import string

with open('string.txt', 'r') as file:
    data = file.read()
print(data)

result=re.findall(r"praveer (.*?) praveer",data)


for i in result:
    print(i)

# !/usr/bin/python

from crossref.restful import Works

works = Works()

w1=works.query('Robust Digital Twin Compositions for Industry 4.0 Smart Manufacturing Systems')
for item in w1:
    print(item['DOI'])