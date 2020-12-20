import csv
import os
f7 = open('D:/REST API file/result/file_category.csv', 'w', newline='')
writer7 = csv.writer(f7)
dirPath="D:/test/category"
for bigcate in os.listdir(dirPath):
    bigCateDir=os.path.join(dirPath, bigcate)
    if os.path.isdir(bigCateDir):
        smallCateDir = os.path.join(bigCateDir, bigcate)
        files=os.listdir(bigCateDir)
        for file in files:
            smallCateDir = os.path.join(bigCateDir, file)
            if os.path.isdir(smallCateDir):
                for f in os.listdir(smallCateDir):
                    writer7.writerow([f,file,bigcate])
            else:
                writer7.writerow([file,bigcate,bigcate])
