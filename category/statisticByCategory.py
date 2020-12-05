import csv
import os

"""
将实验结果按API类别分类
"""

f1 = open('D:/REST API/result/queryPara-all2609940987506606624.csv','r',newline='')
reader1 = csv.reader(f1)

valiall=[]

for row in reader1:
    valiall.append(row)
valiall.sort()

#print(valiall)
path="D:\REST API\\result\\catelist"

for file in os.listdir(path):
    catel=[]
    result = []
    file_path = os.path.join(path, file)
    f = open(file_path,'r',newline='')
    reader = csv.reader(f)
    for row in reader:
        catel.append(row[0])
    catel.sort()
    print(catel)
    f2 = open('D:\REST API\\result\cateValidate\\query-'+file, 'w', newline='')
    writer = csv.writer(f2)
    index=0
    for data in valiall:
        if index<len(catel) and data[0]==catel[index]:
            result.append(data)
            index+=1
#print(catel)
    print(result)
    for k in result:
        writer.writerow(k)
    f2.close()
    f.close()
f1.close()