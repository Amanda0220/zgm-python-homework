# 作业内容
##  1. 使用循环数据集，
###     1. 用 for 循环读入所有csv文件
###     2. 把所有读入的csv数据分别转换成一列向量的形式
###     3. 创建时间和地区的面板数据的表头
###     4. 把表头和41个列向量合并成一个数据框
###     5. 对数据框的变量名进行修改为time, dis和 41 个csv文件的名字
###     6. 把最后得到的数据框写出为csv文件
import numpy as np
import pandas as pd
import os

#获取data路径下的所有文件名
file_list=os.listdir("./data")

#读入csv文件并把每个csv转换成列向量
sheet=pd.DataFrame()
for i in file_list:
    df=pd.read_csv("./data/"+i,encoding="GB2312")
    df_new=df.iloc[:,1:].values.T.reshape(-1)
    sheet[i[:-4]]=df_new

#生成time和dis表头
time_pd=df.columns[1:]
dis_pd=df.iloc[:,0]

dis_np,time_np=np.meshgrid(dis_pd,time_pd)

dis=pd.Series(dis_np.reshape(-1))
time=pd.Series(time_np.reshape(-1))

#表头与数据合并
data=pd.concat([dis,time,sheet],axis=1)

#重命名变量名
name=[]
for i in file_list:
    name.append(i[:-4])

data.columns=["dis","time"]+name

#数据输出
data.to_csv("./data.csv",encoding="gb2312")

##  2. 自定义函数
###     1. 给出一个 list， 求其平均差 $MAD=\frac{1}{n}\sum_{i}^{n}|x_{i}-\bar x_{i}|$
def MAD(Lst):
    mean_Lst=sum (Lst)/len(Lst)
    dif=list()
    for i in Lst:
        dif.append(abs(i-mean_Lst))
    return sum (dif)/len(dif)

a=[9,7,12,66]
MAD(a)

###     2. 编写一个函数opposite，把向量倒置，对某一向量使用该函数
def opposite(vector):
    return vector[::-1]

###     3. 编写一个函数shift，把向量元素右移 k 个位置，对某一向量使用该函数
def shift(vector,k):
    head=list(vector[len(vector)-k:])
    tail=list(vector[:len(vector)-k])
    # for i in tail:
        # head.append(i)
    return head+tail
a=np.array([19,16,20,77,99])
shift(a,2)

###     4. 生成一个20行10列的矩阵，把矩阵的每一列倒置，把矩阵的每一行元素向右3个位置
matr1=np.arange(200).reshape(20,10)
matr2=opposite(matr1)
for i in range(20):
    matr2[i,:]=shift(matr2[i,:],3)
matr2
new_matr=np.array(matr3)

for i in range(10):
    new_matr[:,i]=new_matr[:,i]+i+1
new_matr

###     5. 编写一个函数 fibonacci ，给定一个正整数x, 生成小于x的所有斐波那契数列元素， 求x=10000000时具体数列.
def fibonacci(x):
    a=[1,1]
    b=a[-1]+a[-2]
    while b<=x:
        a.append(b)
        b=a[-1]+a[-2]
    return a
x=10000000
y=fibonacci(x);y

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
