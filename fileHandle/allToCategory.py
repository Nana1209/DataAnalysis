import csv
import copy
f = open('D:\REST API file\\result\\file_category.csv','r',newline='')
reader = csv.reader(f)
f1 = open('D:\REST API file\\result\hasCacheStatic-all4932095607673570634.csv','r',newline='')
reader1 = csv.reader(f1)
f7 = open('D:/REST API file/result/hasCacheStatic-cate.csv', 'w', newline='')
writer7 = csv.writer(f7)
# 文件名：类别
dict={}
for row in reader:
    list=[]
    list.append(row[2])
    dict[row[0]]=list
print(dict)

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
    # print(row)
    list1 = []
    if row[0] in dict:
        # 深拷贝，直接赋值是浅拷贝，是一种引用，会改变被引用的值https://blog.csdn.net/u010712012/article/details/79754132
        list1 = copy.deepcopy(dict[row[0]])
        list1.extend(row[1:])
        print([row[0]] + list1)
        writer7.writerow([row[0]] + list1)