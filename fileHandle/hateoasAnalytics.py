import csv

f = open('D:\REST API file\\result\\contextedRelation-cate.csv','r',newline='')
reader = csv.reader(f)
f7 = open('D:/REST API file/result/contextedRelation-cate-rate.csv', 'w', newline='')
writer7 = csv.writer(f7)
dict={}
for row in reader:
    list=[]
    if row[1] in dict:
        list=dict[row[1]]
    else:
        # sum,hateoasCount
        list=[0,0]
    list[0]+=1
    if row[2]=="TRUE":
        list[1]+=1
    dict[row[1]]=list
for k in dict:
    l=[]
    l.append(dict[k][1] / dict[k][0])
    dict[k].extend(l)
    writer7.writerow([k]+dict[k])
print(dict)