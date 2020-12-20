import csv
f = open('D:\REST API file\\result\\versionLocation-cate1.csv','r',newline='')
reader = csv.reader(f)
f7 = open('D:/REST API file/result/versionLocation-cate-rate1.csv', 'w', newline='')
writer7 = csv.writer(f7)
dict={}
for row in reader:
    list=[]
    if row[1] in dict:
        list=dict[row[1]]
    else:
        # sum,hasVersionCount,inHeaderCount,inQueryCount,inHostCount,inPathCount
        list=[0,0,0,0,0,0]
    list[0]+=1
    if row[2]=="1":
        list[1]+=1
        if row[3]=="TRUE":
            list[2]+=1
        if row[4]=="TRUE":
            list[3]+=1
        if row[5]=="TRUE":
            list[4]+=1
        if row[6]!="1":
            list[5]+=1
    dict[row[1]]=list
for k in dict:
    l=[]
    l.append(dict[k][2]/dict[k][0])
    l.append(dict[k][3] / dict[k][0])
    l.append(dict[k][4] / dict[k][0])
    l.append(dict[k][5] / dict[k][0])
    dict[k].extend(l)
    writer7.writerow([k]+dict[k])
print(dict)