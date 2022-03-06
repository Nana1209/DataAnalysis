import os
import csv
f1 = open('D:\REST API file/result/dynamicLog/consistentStatistics.github.csv', 'r', encoding='utf-8', newline='')
reader = csv.reader(f1)
sum=0
CacheControl = 0
Expires =0
Date = 0
Etag = 0
LastModified = 0
ResponseContentType = 0
hateoas = 0

CacheControl10 = 0
Expires10 = 0
Date10 = 0
Etag10 = 0
LastModified10 = 0
ResponseContentType10 = 0
hateoas10 = 0

ResponseContentType11 = 0
hateoas11 = 0
CacheControl11 = 0
Expires11 = 0
Date11 = 0
Etag11 = 0
LastModified11 = 0
ResponseContentType11 = 0
hateoas11= 0

CacheControl01 = 0
Expires01 = 0
Date01 = 0
Etag01 = 0
LastModified01 = 0
ResponseContentType01 = 0
hateoas01 = 0

CacheControl00 = 0
Expires00 = 0
Date00 = 0
Etag00 = 0
LastModified00 = 0
ResponseContentType00 = 0
hateoas00 = 0

for row in reader:
    sum+=1
    if row[1]=='True':
        CacheControl+=1
        if row[2]=='True':
            CacheControl11+=1
        else:
            CacheControl10+=1
    else:
        if row[2] == 'True':
            CacheControl01 += 1
        else:
            CacheControl00 += 1

    if row[4]=='True':
        Expires+=1
        if row[5]=='True':
            Expires11+=1
        else:
            Expires10+=1
    else:
        if row[5] == 'True':
            Expires01 += 1
        else:
            Expires00 += 1

    if row[7]=='True':
        Date+=1
        if row[8]=='True':
            Date11+=1
        else:
            Date10+=1
    else:
        if row[8] == 'True':
            Date01 += 1
        else:
            Date00 += 1

    if row[10]=='True':
        Etag+=1
        if row[11]=='True':
            Etag11+=1
        else:
            Etag10+=1
    else:
        if row[11] == 'True':
            Etag01 += 1
        else:
            Etag00 += 1

    if row[13]=='True':
        LastModified+=1
        if row[14]=='True':
            LastModified11+=1
        else:
            LastModified10+=1
    else:
        if row[14] == 'True':
            LastModified01 += 1
        else:
            LastModified00 += 1

    if row[16]=='True':
        ResponseContentType+=1
        if row[17]=='True':
            ResponseContentType11+=1
        else:
            ResponseContentType10+=1
    else:
        if row[17] == 'True':
            ResponseContentType01 += 1
        else:
            ResponseContentType00 += 1

    if row[20]=='True':
        if row[19]=='True':
            hateoas11+=1
        else:
            hateoas00+=1
    else:
        if row[19] == 'True':
            hateoas01 += 1
        else:
            hateoas10 += 1

f8 = open('D:\REST API file/result/dynamicLog/static.github.csv', 'w', newline='')
writer8 = csv.writer(f8)
writer8.writerow([sum])
writer8.writerow([CacheControl,Expires,Date,Etag,LastModified,ResponseContentType,hateoas])
writer8.writerow([CacheControl10+CacheControl01,Expires10+Expires01,Date10+Date01,Etag10+Etag01,LastModified10+LastModified01,ResponseContentType10+ResponseContentType01,hateoas10+hateoas01])
writer8.writerow([CacheControl01,Expires01,Date01,Etag01,LastModified01,ResponseContentType01,hateoas01])
writer8.writerow([CacheControl10,Expires10,Date10,Etag10,LastModified10,ResponseContentType10,hateoas10])
writer8.writerow([CacheControl11,Expires11,Date11,Etag11,LastModified11,ResponseContentType11,hateoas11])
writer8.writerow([CacheControl00,Expires00,Date00,Etag00,LastModified00,ResponseContentType00,hateoas00])
