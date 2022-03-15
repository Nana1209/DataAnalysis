import csv
import json
# -*- coding: UTF-8 -*-
f = open('D:/test/result.api.github.com.json','r',encoding='utf-8',newline='')
json_datas=json.load(f)
# print(json_datas)

f8 = open('D:\REST API file/result/dynamicLog/consistentStatistics.github1.csv', 'w', newline='')
writer8 = csv.writer(f8)


for methodPath,pathResult in json_datas['path-dy'].items():
    hasCacheControl=False
    hasExpires=False
    hasDate=False
    hasEtag=False
    hasLastModified=False
    hasResponseContentType=False
    hateoas=False
    isHATEOASdy =False
    if 'hasCacheControl' in pathResult:
        if pathResult['hasCacheControl'] == pathResult['hasCacheControlStatic']:
            hasCacheControl=True
        if pathResult['hasExpires'] ==pathResult['hasExpiresStatic']:
            hasExpires=True
        if pathResult['hasDate']== pathResult['hasDateStatic']:
            hasDate=True
        if pathResult['hasEtag']==pathResult['hasEtagStatic']:
            hasEtag=True
        if pathResult['hasLastModified']==pathResult['hasLastModifiedStatic']:
            hasLastModified=True
        if pathResult['hasContentType']==pathResult['hasResponseContentTypeStatic']:
            hasResponseContentType=True
        if 'isHATEOAS-dy' in pathResult:
            isHATEOASdy=pathResult['isHATEOAS-dy']
        if 'isHATEOAS-dy' in pathResult and pathResult['isHATEOAS-dy']==pathResult['hateoasStatic']:
            hateoas=True
        writer8.writerow([methodPath,
                          pathResult['hasCacheControl'], pathResult['hasCacheControlStatic'], hasCacheControl,
                          pathResult['hasExpires'], pathResult['hasExpiresStatic'], hasExpires,
                          pathResult['hasDate'], pathResult['hasDateStatic'], hasDate,
                          pathResult['hasEtag'], pathResult['hasEtagStatic'], hasEtag,
                          pathResult['hasLastModified'], pathResult['hasLastModifiedStatic'], hasLastModified,
                          pathResult['hasContentType'], pathResult['hasResponseContentTypeStatic'], hasResponseContentType,
                          isHATEOASdy,pathResult['hateoasStatic'], hateoas])

