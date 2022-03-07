import os
import csv
f8 = open('D:\REST API file/result\icstConsistentAnalysis/ruleConsistence.csv', 'w', newline='')
writer8 = csv.writer(f8)
writer8.writerow(['api', 'CacheControl', 'Expires', 'Date', 'Etag', 'LastModified', 'ResponseContentType', 'hateoas'])

file='D:\\REST API file\\result\\icstConsistentStatic'
for root, dirs, files in os.walk(file):

        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list

        # 遍历文件

        for f in files:
            print(f)
            # print(os.path.join(root, f))
            f1 = open(os.path.join(root, f), 'r', encoding='utf-8', newline='')
            reader = csv.reader(f1)
            sum=0

            for i, row in enumerate(reader):
                if i==0:
                    sum=float(row[0])
                if i==2:
                    writer8.writerow([f,float(row[0])/sum,float(row[1])/sum,float(row[2])/sum,float(row[3])/sum,float(row[4])/sum,float(row[5])/sum,float(row[6])/sum])




