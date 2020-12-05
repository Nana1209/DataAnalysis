import csv
import os
import shutil
import sys

f = open('D:\\REST API\\swagger\\validator-badge\\result\\category-openAPIv2.0all.csv','r',newline='')
reader = csv.reader(f)
f1 = open('D:\\REST API\\swagger\\validator-badge\\result\\category-openAPIv3.0all.csv','r',newline='')
reader1 = csv.reader(f1)
catedict={}
for row in reader:
    source ='E:/test/swagger-versionClear-pathClear/'+row[0]
    target = 'E:/test/category/'
    if len(row[1])==0:
        shutil.copy(source, target)
        continue
    for cate in row[1:]:
        if not len(cate) == 0:
            target='E:/test/category/'+cate
            if not os.path.exists(target):
                os.makedirs(target)
            if os.path.exists(source):
                shutil.copy(source, target)
                print(source)
            else:
                print('no '+source)

for row in reader1:
    source = 'E:/test/openapi-versionClear-pathClear/' + row[0]
    target = 'E:/test/category/'
    if len(row[1])==0:
        shutil.copy(source, target)
        continue
    for cate in row[1:]:
        if not len(cate)==0:
            target = 'E:/test/category/' + cate
            if not os.path.exists(target):
                os.makedirs(target)
            if os.path.exists(source):
                shutil.copy(source, target)
                print(source)
            else:
                print('no ' + source)
# source = 'current/test/test.py'
# target = '/prod/new'
#
# assert not os.path.isabs(source)
# target = os.path.join(target, os.path.dirname(source))
#
# # create the folders if not already exists
# os.makedirs(target)
#
# # adding exception handling
# try:
#    shutil.copy(source, target)
# except IOError as e:
#    print("Unable to copy file. %s" % e)
# except:
#    print("Unexpected error:", sys.exc_info())