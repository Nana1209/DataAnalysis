import csv

f = open('D:\REST API file\\result\\statusUsage-cate.csv','r',newline='')
reader = csv.reader(f)
f7 = open('D:/REST API file/result/statusUsage-cate-rate.csv', 'w', newline='')
writer7 = csv.writer(f7)
dict={}
for row in reader:
    list=[]
    if row[1] in dict:
        list=dict[row[1]]
    else:
        # sum,2xxCount,3xxCount,4xxCount,5xxCount
        list=[0,0,0,0,0]
    list[0]+=1
    list[1]+=float(row[7])
    list[2] += float(row[8])
    list[3] += float(row[9])
    list[4] += float(row[10])
    dict[row[1]]=list
for k in dict:
    l=[]
    l.append(dict[k][1] / dict[k][0])
    l.append(dict[k][2]/dict[k][0])
    l.append(dict[k][3] / dict[k][0])
    l.append(dict[k][4] / dict[k][0])
    dict[k].extend(l)
    writer7.writerow([k]+dict[k])
print(dict)