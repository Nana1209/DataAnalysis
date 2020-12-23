import csv
import json

f = open('D:\REST API file\\result\\statusUsage-all.json','r',newline='')
json_datas=json.load(f)
f7 = open('D:/REST API file/result/statusUsage-all.csv', 'w', newline='')
writer7 = csv.writer(f7)
for file in json_datas:
    list=json_datas[file]
    list.append(list[1]/list[0])
    list.append(list[2] / list[0])
    list.append(list[3] / list[0])
    list.append(list[4] / list[0])
    print(file)
    print(list)
    writer7.writerow([file]+list)