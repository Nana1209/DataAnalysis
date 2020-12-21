import csv
f = open('D:\REST API file\\result\\file_category.csv','r',newline='')
reader = csv.reader(f)
f1 = open('D:\REST API file\\result\\token)-all10965381012015188870.csv','r',newline='')
reader1 = csv.reader(f1)
f7 = open('D:/REST API file/result/acceptToken-cate3.csv', 'w', newline='')
writer7 = csv.writer(f7)
dict={}
for row in reader:
    list=[]
    list.append(row[2])
    dict[row[0]]=list
#print(dict)

#version
# for row in reader1:
#     if row[0] in dict:
#         list=dict[row[0]]
#         if row[4]!="1" or row[1]=="TRUE" or row[2]=="TRUE" or row[3]=="TRUE":
#             list.append(1)
#             list.extend(row[1:5])
#
#         else:
#             list.append(0)
#         writer7.writerow([row[0]]+list)

# acceptToken
for row in reader1:
    if row[0] in dict:
        list = dict[row[0]]
        list.extend(row[1:])
        writer7.writerow([row[0]] + list)