import csv
import os
#import pandas as pd

import numpy

f = open('E:\\test\\fileWithCategory-2.csv','r',newline='')
f1=open('D:\\REST API\\swagger\\validator-badge\\result\\category-openAPIv2.07094604234858170130.csv','r',newline='')
f3 = open('D:\\REST API\\swagger\\validator-badge\\result\\category-openAPIv2.0all.csv', 'w',newline='')
# 2. 基于文件对象构建 csv写入对象
writer = csv.writer(f3)
reader = csv.reader(f)
cateInPro=list(reader)
print(cateInPro[0])
reader1=csv.reader(f1)
cateInFile=list(reader1)
print(cateInFile)
catetemp=cateInFile[0][1]
catetemp=catetemp.replace("[","")
catetemp=catetemp.replace("]","")
catetemp=catetemp.replace("]","")
catetemp=catetemp.replace(" ","")
print(catetemp)
print(type(reader))
indexInfile=0
for i in range(len(cateInPro)):
    if cateInPro[i][0]==cateInFile[indexInfile][0]:
        for j in range(1,len(cateInFile[indexInfile])):
            catetemp=cateInFile[indexInfile][j]
            catetemp = catetemp.replace("[", "")
            catetemp = catetemp.replace("]", "")
            catetemp = catetemp.replace("]", "")
            catetemp = catetemp.replace(" ", "")
            cateInFile[indexInfile][j]=catetemp
        print(cateInFile[indexInfile])
        # 3. 构建列表头
        writer.writerow(cateInFile[indexInfile])
        indexInfile = indexInfile + 1
    else:
        writer.writerow(cateInPro[i])
#
# df=pd.read_csv('D:/REST API/swagger/validator-badge/result/category-openAPIv3.0.csv')
# print(df[0])

def deleteFile(name):
    #path = 'F:/新建文本文档.txt'  # 文件路径
    if os.path.exists(name):  # 如果文件存在
        # 删除文件，可使用以下两种方法。
        os.remove(name)
        # os.unlink(path)
    else:
        print('no such file:%s' % name)  # 则返回文件不存在
    return

