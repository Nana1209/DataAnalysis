import csv

f = open('D:\REST API file\\result\\CRUDPathOperations-cate.csv','r',newline='')
reader = csv.reader(f)
f7 = open('D:/REST API file/result/CRUDPathOperationsMistake-cate.csv', 'w', newline='')
writer7 = csv.writer(f7)
mistake=0
for row in reader:
    list=[]
    list.append(row[0])
    list.append(row[1])
    mistake = 0
    if row[5]=='':
        # print(row)
        if row[4]=="GET":
            if row[3]!="get" and row[3]!="read":
                mistake=1
        elif row[4]=="POST":
            if row[3]!="create" and row[3]!="add" and row[3]!="post" and row[3]!="new" and row[3]!="push":
                mistake=1
        elif row[4]=="PUT" or row[4]=="POST":
            if row[3]!="update" and row[3]!="put" and row[3]!="set" and row[3]!="push" and row[3]!="modify":
                mistake=1
        elif row[4]=="DELETE":
            if row[3]!="remove" and row[3]!="delete" and row[3]!="drop":
                mistake=1
    # print(row[0]+str(mistake))
    list.append(mistake)
    list.extend(row[2:])
    print(list)
    writer7.writerow(list)