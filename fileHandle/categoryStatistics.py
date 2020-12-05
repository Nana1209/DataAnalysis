import csv
import json

f = open('D:\\REST API\\swagger\\validator-badge\\result\\category-openAPIv2.0all.csv','r',newline='')
reader = csv.reader(f)
f1 = open('D:\\REST API\\swagger\\validator-badge\\result\\category-openAPIv3.0all.csv','r',newline='')
reader1 = csv.reader(f1)
catedict={}

for row in reader:
    for cate in row[1:]:
        cate=cate.lower()
        if cate in catedict:
            catedict[cate]+=1
        else:
            catedict[cate]=1
for row in reader1:
    for cate in row[1:]:
        cate = cate.lower()
        if cate in catedict:
            catedict[cate]+=1
        else:
            catedict[cate]=1
f = open('E:\\test\\categoryStatistics.csv','w',newline='')
writer = csv.writer(f)
for k in catedict.keys():
    writer.writerow([k,catedict[k]])

# jsObj = json.dumps(catedict)
# f3 = open('D:\\REST API\\swagger\\validator-badge\\result\\categoryStatisticsnew.json', 'w')
# f3.write(jsObj)
print(catedict)
f.close()
f1.close()
#f3.close()