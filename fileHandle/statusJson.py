import csv
import json

f = open('D:\REST API file\\result\\status-all.json','r',newline='')
json_datas=json.load(f)
#print(len(json_datas))

"""
statulines={}
for fileName in json_datas:
    data=json_datas[fileName]
    print(data)
    for status,count in data.items():
        if status in statulines:
            statulines[status]+=count
        else:
            statulines[status]=count
print(statulines)

f7 = open('D:/REST API file/result/statusStatistics.csv', 'w', newline='')
writer7 = csv.writer(f7)
for k,v in statulines.items():
    writer7.writerow([k,v])"""

f7 = open('D:/REST API file/result/status-all.csv', 'w', newline='')
writer7 = csv.writer(f7)
for fileName in json_datas:
    data=json_datas[fileName]
    opcount=data['opcount']
    print(data)
    x2=0
    x3=0
    x4=0
    x5=0
    for status,count in data.items():
        if status[0]=='2':
            x2+=count
        elif status[0]=='3':
            x3+=count
        elif status[0] == '4':
            x4 += count
        elif status[0] == '5':
            x5 += count
    writer7.writerow([fileName,x2,x3,x4,x5,x2/opcount,x3/opcount,x4/opcount,x5/opcount])