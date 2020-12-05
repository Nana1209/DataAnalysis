import csv
import json
import re

import wordninja

f1 = open('D:\REST API\\result\\path-all6366531348915523614.csv','r',newline='')
reader1 = csv.reader(f1)
splitresult={}
for row in reader1:
    pathresults={}
    for i in range(1,len(row)):
        resulttemp=[]
        hirSplitList=row[i].split('/')
        for hir in hirSplitList:
            #print(hir)
            if hir!='' :
                a = re.sub(u"\\{.*?}", "", hir)
                resultfir = wordninja.split(a)
                resulttemp.append(resultfir)

        pathresults[row[i]]=resulttemp
    splitresult[row[0]]=pathresults

print(splitresult)
json_str = json.dumps(splitresult, indent=4)
with open('D:\REST API\\result\\pathsplithir.json', 'w') as json_file:
    json_file.write(json_str)
# print(wordninja.split('authorized Certificates'))
# print(wordninja.split('authorizedCertificates'))
# print(wordninja.split('authorized-Certificates'))
# print(wordninja.split('authorizedcertificates'))
# print(wordninja.split('authorized/certificates'))