import csv

f = open('D:\REST API file\\result\\CRUDPathOperationsMistake-cate.csv','r',newline='')
reader = csv.reader(f)
f7 = open('D:/REST API file/result/CRUDPathOperationsMistake-cate-rate.csv', 'w', newline='')
writer7 = csv.writer(f7)
dict={}
for row in reader:
    list = []
    if row[1] in dict:
        list = dict[row[1]]
    else:
        # sum,mistakeCount
        list = [0, 0]
    list[0] += 1
    list[1] += int(row[2])
    dict[row[1]] = list
for k in dict:
    dict[k].append(dict[k][1] / dict[k][0])
    writer7.writerow([k] + dict[k])
print(dict)
