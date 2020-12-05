import csv
import os

def listdir(path, list_name):  #传入存储的list
  for file in os.listdir(path):
      file_path = os.path.join(path, file)
      if os.path.isdir(file_path):
          listdir(file_path, list_name)
      else:
         list_name.append(file)
cate="search"
listcloud=[]
listdir("E:\\test\category\\"+cate,listcloud)
print(listcloud)
f = open('E:\\test\\'+cate+'list.csv','w',newline='')
writer = csv.writer(f)
for k in listcloud:
    writer.writerow([k])
f.close()