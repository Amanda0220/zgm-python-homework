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

sheet=pd.DataFrame()
for i in name:
    df=pd.read_csv("./data/"+i+".csv",encoding="GB2312")
    sheet=pd.concat([sheet,df],axis=1)
#teacher
for i in file_list:
    if i[-4:]=='.csv':
        name.append(i[:-4])

###     2. 把所有读入的csv数据分别转换成一列向量的形式
import numpy as np

data=pd.DataFrame()
for i in range(41):
    sing=np.array(sheet.iloc[:,(i*11+1):(i+1)*11]).reshape(180,1)
    sing=pd.DataFrame(sing)
    data=pd.concat([data,sing],axis=1)

# teacher
csvfiles=os.listdir("./data")
dat=pd.DataFrame()
for i in csvfiles:
    temp=pd.read_csv("./data/"+i,encoding="GB2312")
    temp1=temp.iloc[:,1:].values.T.reshape(180) #180并不稳健
    dat[i[:-4]]=temp1
#for i in csvfiles:
#    temp=pd.read_csv("./data/"+i,encoding="GB2312")
#    temp1=temp.iloc[:,1:].values.T.reshape(-1) #-1让python自己推演
#    dat[i[:-4]]=temp1


###     3. 创建时间和地区的面板数据的表头
time_cl=sheet.drop(["district"],axis=1)
time_list=list(time_cl.columns[0:10])*18

dis_id=list(sheet.iloc[:,0])
dis_list=list()
for i in dis_id:
    dis_list=dis_list+[i]*10

head=pd.DataFrame([time_list,dis_list]).T

#teacher
year=np.arange(2002,2012)
time=np.repeat(year,18)
dis=temp["district"]
np.tile(dis.values,10)

#head=np.meshgrid(dis,year) #类似于笛卡尔积

dat["Year"]=np.repeat(year,18)
dat['dis']=np.tile(dis,10)

###     4. 把表头和41个列向量合并成一个数据框
data=pd.concat([head,data],axis=1)

###     5. 对数据框的变量名进行修改为time, dis和 41 个csv文件的名字
data.columns=['time','dis']+name

###     6. 把最后得到的数据框写出为csv文件
data.to_csv("./data.csv")

##  2. 自定义函数
###     1. 给出一个 list， 求其平均差 $MAD=\frac{1}{n}\sum_{i}^{n}|x_{i}-\bar x_{i}|$
def MAD(Lst):
    mean_Lst=sum (Lst)/len(Lst)
    dif=list()
    for i in Lst:
        dif.append(abs(i-mean_Lst))
    return sum (dif)/len(dif)

###     2. 编写一个函数opposite，把向量倒置，对某一向量使用该函数
def opposite(vector):
    return vector[::-1]

###     3. 编写一个函数shift，把向量元素右移 k 个位置，对某一向量使用该函数
def shift(vector,k):
    head=list(vector[len(vector)-k:])
    tail=list(vector[:len(vector)-k])
    for i in tail:
        head.append(i)
    return np.array(head)

###     4. 生成一个20行10列的矩阵，把矩阵的每一列倒置，把矩阵的每一行元素向右3个位置
matr1=np.arange(200).reshape(20,10)
matr2=opposite(matr1)
matr3=list()
for i in matr2:
    i=shift(i,3)
    matr3.append(i)
new_matr=np.array(matr3)

###     5. 编写一个函数 fibonacci ，给定一个正整数x, 生成小于x的所有斐波那契数列元素， 求x=10000000时具体数列.
def fibonacci(x):
    a=[1,1]
    for i in range(x):
        b=a[-1]+a[-2]
        if i==b:
            a.append(i)
        else:
            continue
    return a
m=fibonacci(10000000)

##  3. 自定义一个正方形的类：
###     1. 给出其位置和边长属性
class square:
    """正方形"""
    pos=(0,0)
    a=1

###     2. 更改其 __init__ 方法，位置和边长属性默认为(0,0)和1
class square:
    """正方形"""
    def __init__(self,t=(0,0),a=1):
        self.pos=t
        self.l=a

###     3. 更改其 __str__ 方法
class square:
    """正方形"""
    def __init__(self,t=(0,0),a=1):
        self.pos=t
        self.l=a
    def __str__(self):
        return print('正方形:','位置为：',self.pos,'边长为：',self.l)

###     4. 定义一个求其面积的方法
class square:
    """正方形"""
    def __init__(self,t=(0,0),a=1):
        self.pos=t
        self.l=a
    def __str__(self):
        return print('正方形:','位置为：',self.pos,'位置为：',self.l)
    def area(self):
        return self.l**2

###     5. 定义一个两个正方形距离的方法
class square:
    """正方形"""
    def __init__(self,t=(0,0),a=1):
        self.pos=t
        self.l=a
    def __str__(self):
        return print('正方形:','位置为：',self.pos,'位置为：',self.l)
    def area(self):
        return self.l**2
    def dis(self,other):
        return ((self.pos[0]-other.pos[0])**2+(self.pos[1]-other.pos[1])**2)**0.5
