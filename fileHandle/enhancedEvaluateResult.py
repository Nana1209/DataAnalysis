import csv
f = open('D:\project/rester\logs/dynamic.log','r',encoding='utf-8',newline='')

f7 = open('D:\REST API file/result\dynamicLog/enhancedEvaluateResult.csv', 'w',encoding='utf-8', newline='')
writer7 = csv.writer(f7)

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

for resultRow in resultRows:
    print(resultRow[8])
    writer7.writerow(resultRow)
# status={}
# for request in requests:
#     if request[0] in status:
#         status[request[0]].append(request[1:])
#         # print(status[request[0]])
#     else:
#         pathList=[]
#         pathList.append(request[1:])
#         status[request[0]]=pathList
#         # print(status[request[0]])
# print(status)
# statusStatics={}
# for request in requests:
#     if request[5] in statusStatics:
#         statusStatics[request[5]][request[6]]=statusStatics[request[5]].get(request[6],0)+1
#     else:
#         statusTemp={}
#         statusTemp[request[6]]=1
#         statusStatics[request[5]]=statusTemp
# print(statusStatics)
# results=[]
# for k,v in statusStatics.items():
#
#     # print(k)
#     account=0
#     for k1,v1 in v.items():
#         account=account+v1
#     for k1,v1 in v.items():
#         # print(k1,v1)
#         result=[]
#         result.append(k)
#         result.append(k1)
#         result.append(v1)
#         result.append(v1/account)
#         # print(result)
#         results.append(result)
# for result in results:
#     print(result)
#     writer7.writerow(result)