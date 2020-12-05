import csv
import os

import requests
from bs4 import BeautifulSoup

f = open('E:\\test\\fileWithCategory-2.csv','a',newline='') #w写 a追加（a+不存在新建）
writer = csv.writer(f)

for file in os.listdir("E:\\test\swagger-versionClear"):
    print(file) #file是文件名
    filename=os.path.splitext(file)[0]

    keywordtemp=filename.split("-")[0]
    if keywordtemp.find(".")>0:
        suffix=keywordtemp.split(".")[1]
        if suffix=="com" or suffix=="io":
            keyword=keywordtemp[:keywordtemp.index('.')]
        else:
            keyword=keywordtemp
    else:
        keyword=keywordtemp

    kv={"keyword":keyword}
    url ="https://www.programmableweb.com/category/all/apis?keyword="

    r = requests.get(url,params=kv)
    r.encoding = 'utf-8'
    soup=BeautifulSoup(r.text,'html.parser')

    # print(soup.find_all("td",class_="views-field-field-article-primary-category")[0]
    # )
    # category=soup.find("td",class_="views-field-field-article-primary-category").find("a").text

    tds = soup.find_all("td", class_="views-field-field-article-primary-category")
    cate = []
    cate.append(file)
    if len(tds) == 0:
        writer.writerow(cate)
    else:
        for td in tds:
            # print(td.find("a").text)
            a=td.find("a")
            if a!=None:
                cate.append(a.text)
            else:
                cate.append("")
        writer.writerow(cate)
f.close()