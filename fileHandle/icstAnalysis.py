import os
import csv
f8 = open('D:\REST API file/result\icstConsistentAnalysis/ruleAchievedHateoas.csv', 'w', newline='')
writer8 = csv.writer(f8)
writer8.writerow(['api', 'CacheControl', 'Expires', 'Date', 'Etag', 'LastModified', 'ResponseContentType', 'hateoas'])
f9 = open('D:\REST API file/result\icstConsistentAnalysis/ruleconsistenceHateoas.csv', 'w', newline='')
writer9 = csv.writer(f9)
writer9.writerow(['api', 'CacheControl', 'Expires', 'Date', 'Etag', 'LastModified', 'ResponseContentType', 'hateoas'])
f10 = open('D:\REST API file/result\icstConsistentAnalysis/ruleStaticHateoas.csv', 'w', newline='')
writer10 = csv.writer(f10)
writer10.writerow(['api', 'CacheControl', 'Expires', 'Date', 'Etag', 'LastModified', 'ResponseContentType', 'hateoas'])

# file='D:\\REST API file\\result\\icstConsistentStatichateoas'
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
            static0=0
            static1 = 0
            static2 = 0
            static3 = 0
            static4 = 0
            static5 = 0
            static6 = 0
            for i, row in enumerate(reader):
                if i==0:
                    sum=float(row[0])
                # if i==1:
                #     writer8.writerow([f,float(row[0])/sum,float(row[1])/sum,float(row[2])/sum,float(row[3])/sum,float(row[4])/sum,float(row[5])/sum,float(row[6])/sum])
                # if i==2:
                #     writer9.writerow([f,float(row[0])/sum,float(row[1])/sum,float(row[2])/sum,float(row[3])/sum,float(row[4])/sum,float(row[5])/sum,float(row[6])/sum])
                if i==3:
                    static0+=float(row[0])
                    static1 += float(row[1])
                    static2 += float(row[2])
                    static3 += float(row[3])
                    static4 += float(row[4])
                    static5 += float(row[5])
                    static6 += float(row[6])
                if i==5:
                    static0+=float(row[0])
                    static1 += float(row[1])
                    static2 += float(row[2])
                    static3 += float(row[3])
                    static4 += float(row[4])
                    static5 += float(row[5])
                    static6 += float(row[6])
            writer10.writerow([f,static0/sum,static1/sum,static2/sum,static3/sum,static4/sum,static5/sum,static6/sum])


