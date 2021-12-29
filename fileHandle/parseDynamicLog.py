import csv
f = open('D:\project/rester\logs/dynamic.log','r',encoding='utf-8',newline='')

f7 = open('D:\REST API file/result\dynamicLog/gist有序列-有路径属性2-status.csv', 'w',encoding='utf-8', newline='')
writer7 = csv.writer(f7)
f8 = open('D:\REST API file/result\dynamicLog/gist有序列-有路径属性2-static.csv', 'w',encoding='utf-8', newline='')
writer8 = csv.writer(f8)
requests=[]

while True:
    row =f.readline()
    if not row:
        break
    # 没找到就继续
    if row.find("2021-12-09 20:54")==-1 :
        continue
    index=row.find("dynamicResultLog:")
    # print(row)
    if index!=-1:
        request=[]
        request.extend(row[index+17:].split(",,"))
        requests.append(request)
print(requests)
for request in requests:
    writer8.writerow(request)
status={}
for request in requests:
    if request[0] in status:
        status[request[0]].append(request[1:])
        # print(status[request[0]])
    else:
        pathList=[]
        pathList.append(request[1:])
        status[request[0]]=pathList
        # print(status[request[0]])
print(status)
statusStatics={}
for request in requests:
    if request[5] in statusStatics:
        statusStatics[request[5]][request[6]]=statusStatics[request[5]].get(request[6],0)+1
    else:
        statusTemp={}
        statusTemp[request[6]]=1
        statusStatics[request[5]]=statusTemp
print(statusStatics)
results=[]
for k,v in statusStatics.items():

    # print(k)
    account=0
    for k1,v1 in v.items():
        account=account+v1
    for k1,v1 in v.items():
        # print(k1,v1)
        result=[]
        result.append(k)
        result.append(k1)
        result.append(v1)
        result.append(v1/account)
        # print(result)
        results.append(result)
for result in results:
    print(result)
    writer7.writerow(result)