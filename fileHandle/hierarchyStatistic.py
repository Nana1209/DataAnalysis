import csv
"""
进行路径统计：使用两种算法
"""
f3 = open('D:/REST API/result/hierarchy-allv2.csv', 'w', newline='')
writer2 = csv.writer(f3)

with open("D:/REST API/result/path-all6366531348915523614.csv", mode='r') as f:
    reader = csv.reader(f)
    for row in reader:
        result=[]
        max1=0
        avg1=0
        max2 = 0
        avg2 = 0
        amount=0
        result.append(row[0])
        for path in row[1:]:
            amount+=1
            if len(path)>1:
                path=path.rstrip('/') #去除尾/
            hir=path.count('/') #层级数算法1：计算/数
            if hir>max1:
                max1=hir
            avg1+=hir
            hirSubPara=path.count('/')-path.count('{') #层级数算法2：去除属性计算层级（即/数-{数
            if hirSubPara>max2:
                max2=hirSubPara
            avg2+=hirSubPara
        result.append(max1)
        result.append(round(avg1/amount,2))
        result.append(max2)
        result.append(round(avg2/amount,2))
        print(result)
        writer2.writerow(result)
