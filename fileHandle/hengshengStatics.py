import csv
import json
import os, sys
# -*- coding: UTF-8 -*-

f7 = open('D:/REST API file/result/hengsheng.csv', 'w', newline='')
writer7 = csv.writer(f7)

path='D:/REST API file/result/hengsheng/'
dirs=os.listdir( path )
for file in dirs:
    fname='D:\REST API file\\result\hengsheng\\'+file
    print(fname)
    f=open(fname,'r',newline='',encoding='utf-8')
    json_datas = json.load(f)
    if len(json_datas)==0:
        writer7.writerow([file])
        continue
    name=json_datas['name']
    pathnum=json_datas['pathNum']
    endpointnum=json_datas['endpointNum']
    avgh=json_datas['avgHierarchies']
    score=json_datas['score']
    oppost=json_datas['opPOST']/endpointnum
    opget=json_datas['opGET']/endpointnum
    opdelete=json_datas['opDELETE']/endpointnum
    opput=json_datas['opPUT']/endpointnum
    oppatch=json_datas['opPATCH']/endpointnum
    nounderline=json_datas['pathEvaData'][0] / json_datas['pathNum'] * 100
    lowercase=json_datas['pathEvaData'][1] / json_datas['pathNum'] * 100
    noversion=json_datas['pathEvaData'][2] / json_datas['pathNum'] * 100
    noapi=      json_datas['pathEvaData'][3] / json_datas['pathNum'] * 100
    nocrud=json_datas['pathEvaData'][4] / json_datas['pathNum'] * 100
    nosuffix=json_datas['pathEvaData'][5] / json_datas['pathNum'] * 100
    noendslash=json_datas['pathEvaData'][6] / json_datas['pathNum'] * 100
    writer7.writerow([file,name,score,pathnum,endpointnum,avgh,oppost,opget,opput,oppatch,opdelete,nounderline,lowercase,noversion,noapi,nocrud,nosuffix,noendslash])
