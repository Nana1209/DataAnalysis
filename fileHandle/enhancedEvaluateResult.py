import csv
f = open('D:\project/rester\logs/dynamic.log','r',encoding='utf-8',newline='')

# f7 = open('D:\REST API file/result\dynamicLog/enhancedEvaluateResult.csv', 'w',encoding='utf-8', newline='')
# writer7 = csv.writer(f7)

resultRows=[]

while True:
    row =f.readline()
    if not row:
        break
    index1=row.find("dynamicResultLog:")
    index2 = row.find("headerResult:")
    index3 = row.find("entityResult:")
    # print(row)
    # resultRow=[]
    if index1!=-1:
        resultRow=[]
        resultRow.extend(row[index1+17:].split(",,"))
        # resultRows.append(resultRow)
    elif index2!=-1:
        resultRow.extend(row[index2+13:].split(",,"))
    elif index3!=-1:
        resultRow.extend(row[index3 + 13:].split(",,"))
        print(resultRow)
        resultRows.append(resultRow)
print(resultRows[0][7])
count=0
hasCacheSchemeCount=0#resultRow[8]
hasEtagCount=0
hasDateCount=0
hasExpiresCount=0
hasLastModifiedCount=0
hasCacheControlCount=0
hasContentTypeCount=0
contentTypeList={}
isHateoasCount=0
for resultRow in resultRows:
    count+=1
    if resultRow[8]=="true" :
        hasCacheSchemeCount+=1
    if resultRow[9]=="true" :
        hasEtagCount+=1
    if resultRow[10]=="true" :
        hasDateCount+=1
    if resultRow[11]=="true" :
        hasExpiresCount+=1
    if resultRow[12]=="true" :
        hasLastModifiedCount+=1
    if resultRow[13]=="true" :
        hasCacheControlCount+=1
    if resultRow[14]=="true" :
        hasContentTypeCount+=1
        if resultRow[15] in contentTypeList:
            contentTypeList[resultRow[15]]+=1
        else:
            contentTypeList[resultRow[15]]=1
    print(resultRow[16])
    if resultRow[16].startswith('true'):

        isHateoasCount+=1
#     print(resultRow[6])
#     print(resultRow[7])
#     print(resultRow[8])
#     # writer7.writerow(resultRow)
#     # logger.info(
#     #     "headerResult:" + hasCacheScheme + ",," + hasEtag + ",," + hasDate + ",," + hasExpires + ",," + hasLastModified + ",," +
#     #     hasCacheControl + ",," + hasContentType + ",," + contentType);
print(count,hasCacheSchemeCount,hasEtagCount,hasDateCount,hasExpiresCount,hasLastModifiedCount,hasCacheControlCount,hasContentTypeCount,isHateoasCount)
# print(contentTypeList)