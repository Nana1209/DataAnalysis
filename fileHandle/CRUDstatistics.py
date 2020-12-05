import csv
import json

f = open('D:\\REST API\\swagger\\validator-badge\\result\\CRUD-all294841124079917195.csv','r',newline='')
reader = csv.reader(f)

CRUDdict={}

for row in reader:
    for cate in row[1:]:
        if cate in CRUDdict:
            CRUDdict[cate]+=1
        else:
            CRUDdict[cate]=1

f1 = open('E:\\test\\CRUDStatisticsv4.0.csv','w',newline='')
writer = csv.writer(f1)
for k in CRUDdict.keys():
    writer.writerow([k,CRUDdict[k]])

# jsObj = json.dumps(catedict)
# f3 = open('D:\\REST API\\swagger\\validator-badge\\result\\categoryStatisticsnew.json', 'w')
# f3.write(jsObj)
print(CRUDdict)
f.close()
f1.close()
#f3.close()