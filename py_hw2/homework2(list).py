# 作业内容
##  1. 使用循环数据集，
###     1. 用 for 循环读入所有csv文件
import pandas as pd
import os

file_list=os.listdir("./data")

name=list()
for i in file_list:
    pos_split=os.path.splitext(i)
    if pos_split[1]=='.csv':
        name.append(pos_split[0])

sheet=list()
for i in name:
    df=pd.read_csv("./data/"+i+".csv",encoding="GB2312")
    sheet.append(df)

###     2. 把所有读入的csv数据分别转换成一列向量的形式
import numpy as np

data=pd.DataFrame()
ns=list()
for i in range(41):
    a=np.array(sheet[i].iloc[:,1:11])
    ns=pd.DataFrame(a.reshape(180,1))
    data=pd.concat([data,ns],axis=1)

###     3. 创建时间和地区的面板数据的表头
time=sheet[0].columns[1:]
time=pd.DataFrame(list(time)*18)

dis=list(sheet[0].iloc[:,0])

area=list()
for i in dis:
    d=list()
    d.append(i)
    d=d*10
    for j in d:
        area.append(j)
area=pd.DataFrame(area)

head=pd.concat([time,area],axis=1)

###     4. 把表头和41个列向量合并成一个数据框
full=pd.concat([head,data],axis=1)

###     5. 对数据框的变量名进行修改为time, dis和 41 个csv文件的名字
full.columns=["time","dis"]+name

###     6. 把最后得到的数据框写出为csv文件
full.to_csv("./full.csv")



