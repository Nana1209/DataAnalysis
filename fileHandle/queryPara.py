import csv

f = open('D:\\REST API\\result\\queryPara-all2609940987506606624.csv','r',newline='')
reader = csv.reader(f)

paradict={}
shixiannum=0
for row in reader:
    if not row[1]=='':
        shixiannum+=1
        for cate in row[1:]:
            if cate in paradict:
                paradict[cate]+=1
            else:
                paradict[cate]=1

f1 = open('D:\\REST API\\result\\queryParaStatistic-all.csv','w',newline='')
writer = csv.writer(f1)
for k in paradict.keys():
    writer.writerow([k,paradict[k]])

# jsObj = json.dumps(catedict)
# f3 = open('D:\\REST API\\swagger\\validator-badge\\result\\categoryStatisticsnew.json', 'w')
# f3.write(jsObj)
print(shixiannum)
print(paradict)
f.close()
f1.close()
#f3.close()