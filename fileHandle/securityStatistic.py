import csv
import json

f = open('D:\\REST API\\swagger\\validator-badge\\result\\security-v2.03781946110160745780.csv','r',newline='')
reader = csv.reader(f)
f1 = open('D:\\REST API\\swagger\\validator-badge\\result\\security-v3.03728676635139631361.csv','r',newline='')
reader1 = csv.reader(f1)
secudict={}
nullSum=0
sum=0
for row in reader:
    sum+=1
    if row[1]=="":
        nullSum += 1
        continue
    for cate in row[1:]:
        if cate != "":
            if cate in secudict :
                secudict[cate]+=1
            else:
                secudict[cate]=1
for row in reader1:
    sum += 1
    if row[1]=="":
        nullSum += 1
        continue
    for cate in row[1:]:
        if cate != "":
            if cate in secudict :
                secudict[cate]+=1
            else:
                secudict[cate]=1

print(secudict)
print(nullSum)
print(sum)

f.close()
f1.close()

# jsObj = json.dumps(secudict)
# f3 = open('D:\\REST API\\swagger\\validator-badge\\result\\securityStatistics.json', 'w')
# f3.write(jsObj)
# f3.close()