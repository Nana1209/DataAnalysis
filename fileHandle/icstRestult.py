import os
import csv
import json
file='D:\\REST API file\\result\\icstResultheteoas'
for root, dirs, files in os.walk(file):

        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list

        # 遍历文件
        for f in files:
            # print(f)
            # print(os.path.join(root, f))
            f1 = open(os.path.join(root, f), 'r', encoding='utf-8', newline='')
            json_datas = json.load(f1)
            print(os.path.join(root, f))
            f8 = open('D:\REST API file/result\icstConsistentResultheteoas/consistent.'+f+".csv", 'w', newline='')
            writer8 = csv.writer(f8)

            for methodPath, pathResult in json_datas['path-dy'].items():
                hasCacheControl = False
                hasExpires = False
                hasDate = False
                hasEtag = False
                hasLastModified = False
                hasResponseContentType = False
                hateoas = False
                isHATEOASdy = False
                if 'hasCacheControl' in pathResult:
                    if pathResult['hasCacheControl'] == pathResult['hasCacheControlStatic']:
                        hasCacheControl = True
                    if pathResult['hasExpires'] == pathResult['hasExpiresStatic']:
                        hasExpires = True
                    if pathResult['hasDate'] == pathResult['hasDateStatic']:
                        hasDate = True
                    if pathResult['hasEtag'] == pathResult['hasEtagStatic']:
                        hasEtag = True
                    if pathResult['hasLastModified'] == pathResult['hasLastModifiedStatic']:
                        hasLastModified = True
                    if pathResult['hasContentType'] == pathResult['hasResponseContentTypeStatic']:
                        hasResponseContentType = True
                    if 'isHATEOAS-dy' in pathResult:
                        isHATEOASdy = pathResult['isHATEOAS-dy']
                    if 'isHATEOAS-dy' in pathResult and pathResult['isHATEOAS-dy'] == pathResult['hateoasStatic']:
                        hateoas = True
                    writer8.writerow([methodPath,
                                  pathResult['hasCacheControl'],pathResult['hasCacheControlStatic'],hasCacheControl,
                                  pathResult['hasExpires'] , pathResult['hasExpiresStatic'],hasExpires,
                                  pathResult['hasDate'] , pathResult['hasDateStatic'],hasDate,
                                  pathResult['hasEtag'] , pathResult['hasEtagStatic'],hasEtag,
                                  pathResult['hasLastModified'], pathResult['hasLastModifiedStatic'],hasLastModified,
                                  pathResult['hasContentType'] , pathResult['hasResponseContentTypeStatic'],hasResponseContentType,
                                  isHATEOASdy,pathResult['hateoasStatic'],hateoas])


