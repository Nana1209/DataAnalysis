import csv
import json

import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet as wn
from numpy import array
from gensim.models import Word2Vec


f3 = open('D:\\REST API\\swagger\\validator-badge\\result\\categoryStatisticsnew.json', 'r')
js=json.load(f3)
print(type(js))
keys=list(js.keys())
# keys.remove("")
wordlists=[]
for i in range(len(keys)):
    keys[i]=keys[i].lower()
    keys[i] = keys[i].replace(" ", "_")
    listtemp=[]
    listtemp.append(keys[i])
    wordlists.append(listtemp)
#print(wordlists)

cates=sorted(js.items(),key=lambda d:d[1],reverse=True)
print(cates)
#print(wn.synsets('media'))

media=wn.synsets('media')[0]
print(wn.synsets('e-commerce'))
ecommerce=wn.synsets('e-commerce')[0]
marketing=wn.synsets('marketing')[0]
payment=wn.synsets('payment')[0]
print(wn.synsets('search')[0].path_similarity(wn.synsets('sports')[0]))
print(ecommerce.path_similarity(payment))
wnlist=[]
for cate in cates:
    wnlist.append(cate[0])
print(wnlist)
wnlist[1]='data'
wnlist[2]='developer'
wnlist[5]='e-commerce'
wnlist[6]='finance'
wnlist[13]='server'
wnlist[18]='analysis'
wnlist[22]='controller'
wnlist[23]='algorithm'
wnlist[31]='time'
wnlist[33]='management'
wnlist[34]='application'
wnlist[37]='platform'
wnlist[44]='management'
wnlist[48]='management'
wnlist[52]='estate'
wnlist[55]='management'
synsetList=[]
for cate in wnlist:
    print(cate)
    synsetList.append(wn.synsets(cate)[0])
print(synsetList)
f = open('E:\\test\\categoryAnalysis.csv','w',newline='')
writer = csv.writer(f)
disList=[]
disList.append(wnlist)
writer.writerow(wnlist)
for syn in synsetList:
    distemp=[]
    for syntemp  in synsetList:
        distemp.append(syn.path_similarity(syntemp))
    disList.append(distemp)
    writer.writerow(distemp)
print(disList)
f.close()

