import csv
import os
"""
针对不同实验内容进行结果自动统计分析
"""
# f1 = open('D:/REST API/result/basicInfoResult.csv', 'w', newline='')
# writer = csv.writer(f1)
# f2 = open('D:/REST API/result/securityResult.csv', 'w', newline='')
# writer2 = csv.writer(f2)
# f3 = open('D:/REST API/result/hierarchyResult.csv', 'w', newline='')
# writer3 = csv.writer(f3)
# f4 = open('D:/REST API/result/valiationResult.csv', 'w', newline='')
# writer4 = csv.writer(f4)
# f5 = open('D:/REST API/result/CRUDResult.csv', 'w', newline='')
# writer5 = csv.writer(f5)
# f6 = open('D:/REST API/result/queryResult.csv', 'w', newline='')
# writer6 = csv.writer(f6)
f7 = open('D:/REST API/result/suffixResult.csv', 'w', newline='')
writer7 = csv.writer(f7)

path='D:/REST API/result/cateValidate'
for file in os.listdir(path):
    file_path = os.path.join(path, file)
    if file.startswith('basicInfo'):
        account=0
        pathAvg=0
        endpointAvg=0
        get=0
        post=0
        delete=0
        put=0
        head=0
        patch=0
        option=0
        trace=0

        with open(file_path, mode='r') as f:
            reader = csv.reader(f)
            catename= file[10:len(file)-8]
            for row in reader:
                account+=1
                pathAvg+=float(row[1])
                endpointAvg+=float(row[2])/float(row[1])
                get+=float(row[3])/float(row[2])
                post+=float(row[4])/float(row[2])
                delete+=float(row[5])/float(row[2])
                put+=float(row[6])/float(row[2])
                head+=float(row[7])/float(row[2])
                patch+=float(row[8])/float(row[2])
                option+=float(row[9])/float(row[2])
                # trace+=float(row[10])/float(row[2])
            # print(len(file),catename)

            result=[catename,pathAvg/account,endpointAvg/account,get/account,post/account,delete/account,put/account,head/account,patch/account,option/account,trace/account]
            # print(result)
            # writer.writerow(result)
    elif file.startswith('security'):
        amount=0
        basic=0
        apiKey=0
        oauth2=0
        http=0


        with open(file_path, mode='r') as f:
            reader = csv.reader(f)
            catename= file[9:len(file)-8]
            shixiannum = 0
            for row in reader:
                amount+=1
                if not row[1] == '':
                    shixiannum += 1
                    for s in row[1:]:
                        if s=='apiKey':
                            apiKey+=1
                        elif s=='basic':
                            basic+=1
                        elif s=='oauth2':
                            oauth2+=1
                        elif s=='http':
                            http+=1


            sesum=apiKey+basic+oauth2+http
            result=[catename,str(shixiannum/amount*100)[:4]+ '%',str(apiKey)+'('+str(apiKey/sesum*100)[:4]+ '%'+')',str(basic)+'('+str(basic/sesum*100)[:4]+ '%'+')',str(oauth2)+'('+str(oauth2/sesum*100)[:4]+ '%'+')',str(http)+'('+str(http/sesum*100)[:4]+ '%'+')']
            # print(result)
            # writer2.writerow(result)
    elif file.startswith('hierarchyV2'):
        avg1 = 0
        maxAll1 = 0
        maxAvg1 = 0
        avg2=0
        maxAll2 = 0
        maxAvg2 = 0
        amount = 0
        with open(file_path, mode='r') as f:
            reader = csv.reader(f)
            catename = file[12:len(file) - 8]

            for row in reader:
                amount+=1
                if float(row[1])>maxAll1:
                    maxAll1=float(row[1])
                if float(row[3])>maxAll2:
                    maxAll2=float(row[3])
                if float(row[2])>maxAvg1:
                    maxAvg1=float(row[2])
                if float(row[4])>maxAvg2:
                    maxAvg2=float(row[4])
                avg1+=float(row[2])
                avg2+=float(row[4])


            result = [catename, round(avg1/amount,2),maxAll1,maxAvg1,round(avg2/amount,2),maxAll2,maxAvg2]
            # print(result)
            # writer3.writerow(result)
    elif file.startswith('validationRate'):
        amount=0
        a0 = [0,0,0,0,0,0,0]
        avg=[0, 0, 0, 0, 0, 0, 0]
        a1 = [0, 0, 0, 0, 0, 0, 0]
        result=[]
        with open(file_path, mode='r') as f:
            reader = csv.reader(f)
            catename = file[15:len(file) - 8]

            for row in reader:
                amount += 1
                for i in range(1,len(row)):
                    avg[i-1]+=float(row[i])
                    if row[i]=='0':
                        a0[i-1]+=1
                    elif row[i]=='1':
                        a1[i-1]+=1
            result.append(catename)
            for i in range(0,7):
                result.append("%.2f%%" % (a1[i]/amount*100)) #完全实现占比
                result.append("%.2f%%" % (avg[i] / amount * 100)) #平均实现率
                result.append("%.2f%%" % (a0[i] / amount * 100))  #未实现占比
            # print(result)
            # writer4.writerow(result)
    elif file.startswith('CRUD'):
        amount=0
        result=[]
        with open(file_path, mode='r') as f:
            reader = csv.reader(f)
            catename = file[5:len(file) - 8]
            CRUDdict = {}
            result.append(catename)
            for row in reader:
                for cate in row[1:]:
                    if cate in CRUDdict:
                        CRUDdict[cate] += 1
                    else:
                        CRUDdict[cate] = 1
            CRUDdicts=sorted(CRUDdict.items(), key = lambda kv:(kv[1], kv[0]), reverse = True)
            # print(CRUDdicts)
            result.append(CRUDdicts)
            # print(result)
            # writer5.writerow(result)
    elif file.startswith('query'):
        amount = 0
        result = []
        with open(file_path, mode='r') as f:
            reader = csv.reader(f)
            catename = file[6:len(file) - 8]
            result.append(catename)
            paradict = {}
            shixiannum = 0
            for row in reader:
                amount+=1
                if not row[1] == '':
                    shixiannum += 1
                    for cate in row[1:]:
                        if not cate=='':
                            if cate in paradict:
                                paradict[cate] += 1
                            else:
                                paradict[cate] = 1

            paradict = sorted(paradict.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
            # print(paradict)
            result.append("%.2f%%" % (shixiannum/amount*100))
            result.append(paradict)

            # print(result)
            # writer6.writerow(result)
    elif file.startswith('suffix'):
        amount=0
        result=[]
        with open(file_path, mode='r') as f:
            reader = csv.reader(f)
            catename = file[7:len(file) - 8]
            CRUDdict = {}
            result.append(catename)
            for row in reader:
                for cate in row[1:]:
                    if not cate=='':
                        if cate in CRUDdict:
                            CRUDdict[cate] += 1
                        else:
                            CRUDdict[cate] = 1
            CRUDdicts=sorted(CRUDdict.items(), key = lambda kv:(kv[1], kv[0]), reverse = True)
            # print(CRUDdicts)
            result.append(CRUDdicts)
            print(result)
            writer7.writerow(result)
# f1.close()
#f2.close()
# f3.close()
# f4.close()
# f5.close()
# f6.close()
f7.close()