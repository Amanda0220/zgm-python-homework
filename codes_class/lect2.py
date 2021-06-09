####################20200312###############
who
x=10
who

y=20
who
del y
who

n=10
n

print(n)
print("n=",n)

10>3
10<3

s='I <3 coding'

s[0:4]
#选取第1个数到第4个数（不包括4，实际上是0切到3），从左至右切片以0开始，从右至左切片以-1开始。
s[2:4]
len(s)
s[2:11]
s[2:12]
s[2:]

s[-3:]
s[-3:-2]

dir(s)
s.count("i")
s.upper() #字母大写

s+s
s+', '+s
s*2

float('nan')

import math
math.pi
int(math.pi)

x=int(3)
float(x)
str(x)
chr(x)

type(x)

import numpy as np
y=np.long(3)
type(y)

list1=['Python',786,2.23,'R',70.2]
list1

[1,4,9,16,25][0:3]
[1,4,9,16,25][3]
[1,4,9,16,25][1]

x=[1,4,9,16,25]
type(x)
dir(x)
x.append(36)
x

y=(1,4,9,16,25)
type(y)
dir(y)

score={'math':85,'stat':90,'computer':80}

score['stat']
score['stat','math']


################20200319#######################

import numpy as np
a=[1,4,9,16]
type(a)
sum(a)
dir(a)
x=np.array(a)
type(x)
sum(x)
dir(x)
a
x
x.var()
a.var() #报错，a不存在var操作
x.mean()

###生成数据
np.arange(1:10) #报错
np.arange(10)+1
np.arange(101,200) #不包括右边200
np.arange(101,201,step=0.5)
np.linspace(101,200,num=300) #linspace包括右边的200
np.linspace(1,1,100)

np.random.seed(10) #使得随机数可以预测，当我们设置相同的seed时，每次生成的随机数相同；反之，不同
np.random.randint(1,9,20) #randint随机生成整数
np.random.rand(10) #rand生成[0,1)之间均匀分布的数
np.random.randn(10) #返回一组样本，具有标准正态分布
np.random.randn(10).var()
np.random.normal(2,3,100)
np.random.normal(2,3,100).var()

np.array([[1,2],[3,4],[5,6]]) #一维是一个列向量
np.random.seed(1234)
np.random.randint(1,10,size=(5,4))
A=np.arange(12).reshape((4,3))
A
A.reshape((2,6),order='C'

A.shape #查看A是几阶矩阵
np.empty((3,3)) #空的矩阵
np.ones((4,3)) #都是1的矩阵
np.zeros((4,3)) #零矩阵
np.eye(4) #单位阵是方阵，只要输入一个
np.diag(np.arange(1,5)) #对角阵
np.diag([1,2,3,4])

import pandas as pd #pandas建立在numpy之上
pd.Series()  #常用于生成（时间）序列

x=[1,2,3,4]
y=[8,10,20,16,5]
type(x)
type(y)

x1=np.array(x)
y1=np.array(y)
type(x1)
type(y1)

x2=pd.Series(x)
y2=pd.Series(y)
type(x2)
type(y2)

dir(x1)
dir(x2)

pd.concat([x2,y2])
y2[2]
y2[1:4]

x=[[1,2],[3,4],[5,6]]
type(x)
x1=np.array([[1,2],[3,4],[5,6]])
type(x1)
pd.DataFrame(x) #有列名有行名

x2=pd.DataFrame(x1)
type(x2)
dir(x2)

y1={'name':['zhang','wang','zhao'],'stat':[80,70,90],'math':[90,94,88],'comp':[85,92,83]}
score=pd.DataFrame(y1)
type(y1)
y1.keys()
y1.values()

score['english']=[89,70,90]
score
score['sports']=[80,np.nan,90]
del score['comp']
score

score.isnull().sum()
score.mean

score.dropna()
dir(score)

score.sort_index()
score.sort_index(axis=1)

score.sort_values(by='stat')


################20200326##################
import pandas as pd
BSdata=pd.read_csv("./data/BSdata.csv",encoding="utf-8") #.表示当前文件夹
type(BSdata)

BSdata2=pd.read_excel("./data/DaPy_data.xlsx","BSdata")
BSdata3=pd.read_excel('./data/DaPy_data.xlsx','QTdata') #括号中的BSdata、QTdata表示工作簿中具体的sheet，也可省略表示默认第一个sheet
BSdata4=pd.read_excel('./data/DaPy_data.xlsx',3)  #第一个开始是0,3表示第4个sheet

# dat=pd.read_clipboard()

BSdata
del BSdata['学号']

BSdata.to_csv('new.csv') #默认保存在当前工作文件夹codes下，文件编码默认为UTF-8
BSdata.to_csv('./data/new.csv')
BSdata.to_excel('./data/new.xlsx')

BSdata=pd.read_excel("./data/DaPy_data.xlsx",0)
# type(BSdata)
# dir(BSdata)

BSdata.info()
BSdata.head() #默认查看前面5条数据
BSdata.tail() #默认查看倒数5条数据
BSdata.head(10) 
BSdata.tail(8)

BSdata.sort_values('支出') #按照支出从小到大排序
BSdata.sort_values('支出',ascending=False) #按照支出降序排列
BSdata.sort_index(axis=1,ascending=False) #将变量名排序，若是英文则按照首字母顺序排列，中文不知。。。

BSdata.index
BSdata.columns #列出变量名字
BSdata.shape
type(BSdata.shape) #BSdata.shape是元组
BSdata.shape[0] #显示行数
BSdata.shape[1] #显示列数

import numpy as np
A=np.random.randint(0,10,size=(10,5))
A.shape
A.reshape(25,2)

BSdata['体重指数']=BSdata.体重/(BSdata.身高/100)**2
#或 BSdata['体重指数']=BSdata['体重']/(BSdata['身高']/100)**2

BSdata.T #转置，但是转置后BSdata并没有被修改
dir(BSdata)

B=np.random.randint(0,10,size=(10,5))

A=pd.DataFrame(A)
B=pd.DataFrame(B)

pd.concat([A,B],axis=0) #AB按行合并，axis=1按列合并

###################20200402###################
import pandas as pd
#### 自己选取

### 选取单个变量
BSdata.info()
BSdata.支出

BSdata['支出']
BSdata[['支出','性别']] #外面的[]取数据集的子集，里面的[]是个list

BSdata[['学号','课程']]

BSdata.iloc[1,3] #第2行第4列
BSdata.iloc[0:10,0:4]
BSdata.iloc[0:10,] #省略表示都要
BSdata.iloc[:10,]  #0也可省略
BSdata.iloc[:5,[1,3,5]] #不连续的用list[]
BSdata.iloc[[1,3,5],[1,3]]

BSdata.iloc[:10,][['性别','支出']]
#BSdata.iloc[:10,['性别','支出']] #错误，不支持
BSdata.loc[:10,['性别','支出']] #loc支持变量名，iloc只支持数字表示的行列

### 条件选取
BSdata[BSdata.支出>40]
BSdata[(BSdata.支出>40)&(BSdata.性别=='女')]
#注意双等号
BSdata[(BSdata.支出>40)&(BSdata.性别=='女')][['性别','支出']]
BSdata.loc[(BSdata.支出>40)&(BSdata.性别=='女'),['性别','支出']]

import numpy as np

dat=np.random.randint(0,100,size=(50,8))
dat[1,3]
dat[1:5,[1,3,5]] #array格式的不需用iloc，其余方面一致

x=[1,4,9,12,39,14]
x[2:5]
x[[1,4]] #list不支持取不连续的,可转化为array来取不连续的
np.array(x)[[1,4]] #注意两个括号[[]]

######################20200409####################
## if语句
a=50

if a>100:
    print("数值大于100")
    print(a)
if a>100:
    print("数值大于100")
print(a)
#是否tab很重要，决定了该语句归属于谁

if a>100:
    print("数值大于100")
else:
    print("数值小于等于100")

print("数值大于100") if a>100 else print(a)
#else不能缺少

## for循环语句
for i in range(1,11):
    print(i)

import string
string.ascii_lowercase
for i in string.ascii_lowercase:
    print(i)
#产生abcdefg……

import pandas as pd
BSdata=pd.read_excel("./data/DaPy_data.xlsx",0)
BSdata.columns
for i in BSdata.columns:
    print(i)

import numpy as np
x=np.random.randint(-10,10,15)
for i in x:
    if i>=0:
        print(i**0.5)
    else:
        break
#break终止循环
for i in x:
    if i>=0:
        print(i**0.5)
    else:
        continue
#continue循环下一个i

y=[1,8,3,19,20,-4,5,2,8,47]
np.array(y).mean()
type(y)
len(y)

sum(y)
mean(y) #error

## 定义均值函数
y.__len__()
len(y)
def mean(Lst):
    return sum (Lst)/len(Lst)
mean(y)

## 定义减法
y2=list()
for i in y:
    y2.append(i-1)

def vsub(Lst,x):
    res=list()
    for i in Lst:
        res.append(i-x)
    return res
vsub(y,1)

## 定义离差平方
def ssq(Lst,x):
    res=list()
    for i in Lst:
        res.append((i-x)**2)
    return res

## 定义方差函数
### 法1
def var1(Lst):
    Lst_mean=mean(Lst)
    var=0
    for i in Lst:
        var=var+(i-Lst_mean)**2
    return var/len(Lst)
var1(y)
### 法2
def var2(Lst):
    """计算方差"""
    Lst_mean=mean(Lst)
    return sum(ssq(Lst,Lst_mean))/(len(Lst)-1)
var2(y)

## 与np.var的比较
import numpy as np
np.var(y) #总体方差
np.var(y,ddof=1) #样本方差

###################20200416##############################
type(ssq)
type(y)

## class
class Myclass:
    """第一个类"""
    i=1234
    def f(self):
        print("Hello World")

a=Myclass()
type(a)
dir(a)
a.i
a.f()

class circle1:
    """一个二维平面中的圆"""
    pos=(0,0)
    r=1

b=circle1()
type(b)
dir(b)
b.pos
b.r

class circle2:
    """一个二维平面中的圆"""
    def __init__(self,t=(0,0),x=1):
        self.pos=t
        self.r=x
    def __str__(self):
        return print('圆:','位置为：',self.pos,'半径为：',self.r)

c=circle2((1,1),10)
c.pos
c.r

d=circle2()
d.pos

g=circle2((1,2),20)
dir(g)
g.__doc__
g.__str__()
print(g)

## 定义方法与定义函数
### 定义函数
import numpy as np
def c_area(x):
    return np.pi*x.r**2
c_area(g)

### 定义方法
class circle3:
    """一个二维平面中的圆"""
    def __init__(self,t=(0,0),x=1):
        self.pos=t
        self.r=x
    def __str__(self):
        return print('圆:','位置为：',self.pos,'半径为：',self.r)
    def area(self):
        return np.pi*self.r**2

h=circle3((1,1),4)
dir(h)
h.area()
type(h.area)
type(c_area)
type(h.pos)

#### 定义两圆的距离
class circle4:
    """一个二维平面中的圆"""
    def __init__(self,t=(0,0),x=1):
        self.pos=t
        self.r=x
    def __str__(self):
        return print('圆:','位置为：',self.pos,'半径为：',self.r)
    def area(self):
        return np.pi*self.r**2
    def dis2(self,other):
        return ((self.pos[1]-other.pos[1])**2+(self.pos[0]-other.pos[0])**2)**0.5

j=circle4((1,1),4)
k=circle4((3,8),3)
j.dis2(k)

