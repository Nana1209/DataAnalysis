import csv

f = open('D:\REST API file\\result\\versionLocationDot-all4030943757985475098.csv','r',newline='')
reader = csv.reader(f)
count=0
for row in reader:
    if row[4]=="TRUE":
        count+=1
print(count)