import csv

f = open('D:\REST API file\\result\\CRUDPathOperationsMistake-cate1.csv','r',newline='')
reader = csv.reader(f)
f7 = open('D:/REST API file/result/CRUDPathOperationsMistake-cate-rate1.csv', 'w', newline='')
writer7 = csv.writer(f7)
dict={}
for row in reader:
    list = []
    if row[1] in dict:
        list = dict[row[1]]
    else:
        # sum,mistakeCount,mistakeGET,POST,DELETE,PUT,PATCH
        list = [0, 0,0,0,0,0,0]
    list[0] += 1
    if int(row[2])==1:

        list[1] += int(row[2])
        if row[3]=="GET":
            list[2]+=1
        elif row[3]=="POST":
            list[3]+=1
        elif row[3]=="DELETE":
            list[4]+=1
        elif row[3]=="PUT":
            list[5]+=1
        elif row[3]=="PATCH":
            list[6]+=1
    dict[row[1]] = list
for k in dict:
    dict[k].append(dict[k][1] / dict[k][0])
    dict[k].append(dict[k][2] / dict[k][0])
    dict[k].append(dict[k][3] / dict[k][0])
    dict[k].append(dict[k][4] / dict[k][0])
    dict[k].append(dict[k][5] / dict[k][0])
    dict[k].append(dict[k][6] / dict[k][0])
    writer7.writerow([k] + dict[k])
print(dict)
