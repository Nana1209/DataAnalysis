import csv
# f = open('D:\REST API file/result\dynamicLog/log1123.csv','r',encoding='utf-8',newline='')
f = open('D:\project/rester\logs/dynamic.log','r',encoding='utf-8',newline='')
reader = csv.reader(f)
f7 = open('D:\REST API file/result\dynamicLog/dynamicLog1123status.csv', 'w', newline='')
writer7 = csv.writer(f7)
f8 = open('D:\REST API file/result\dynamicLog/dynamicLog1123-static.csv', 'w', newline='')
writer8 = csv.writer(f8)
requests=[]

for row in reader:
    print(row[0].find("https"))
    print(row[1].find("status:"))
    print(row)
    request=[]
    request.extend(row[0][89:].split(",,"))
    request.extend(row[1][96:].split(",,"))
    requests.append(request)
    # print(request)
status={}
for request in requests:
    # print(request)
    # print(request[3])
    status[request[4]]=status.get(request[4],0)+1
for k,v in status.items():
    writer7.writerow([k,v]);
for request in requests:
    writer8.writerow(request)
# print(status)