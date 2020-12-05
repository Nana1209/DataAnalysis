import csv
import json

import nltk
def wortag():
    with open('D:\REST API\\result\\wordTagWord.json', 'r') as f:
      tagresult = json.load(f)

    result={}
    for apiname,v in tagresult.items():
        pathresults={}
        for pathname,wordtaglist in v.items():
            verblist=[]
            for hirlist in wordtaglist:
                for hir in hirlist:
                    if hir[1]=='VB' or hir[1]=='VBP' or hir[1]=='VBZ':
                        verblist.append(hir)
            if len(verblist)>0:
                pathresults[pathname]=verblist
        if len(pathresults)>0:
            result[apiname]=pathresults
    json_str = json.dumps(result, indent=4)
    with open('D:\REST API\\result\\verbRefineWord.json', 'w') as json_file:
        json_file.write(json_str)
# wortag()
with open('D:\REST API\\result\\verbRefineWord.json', 'r') as f:
    tagresult = json.load(f)

verList={}
for apiname,v in tagresult.items():
    for pathname,wordtaglist in v.items():
        for vb in wordtaglist:
            word=vb[0].lower()
            if word in verList:
                verList[word] += 1
            else:
                verList[word] = 1

print(verList)
f1 = open('D:\REST API\\result\\verbstatistic-spreWord.csv','w',newline='')
writer = csv.writer(f1)
for k in verList.keys():
    writer.writerow([k,verList[k]])