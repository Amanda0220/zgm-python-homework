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

print("n=", n)


10>3

10<3

s='I <3 coding'

s[0:4]
s[2:4]

len(s)

s[2:11]
s[2:12]
s[2:]

s[-3:]

dir(s)

s.count('i')
s.upper()

s+', '+s
s*10

float('nan')+3

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

y
x
type(x)
type(y)

[1,4,9,16,25][1:3]

[1,4,9,16,25][3]

[1,4,9,16,25][1,3]

x=[1,4,9,16,25]

type(x)
dir(x)

x.append(36)

y=(1,4,9,16,25)
type(y)
dir(y)

score={'math':85, 'stat': 90, 'com': 80}
score={'stat': 90, 'math':85, 'com': 80}

score['stat']
score['stat', 'math']

dir(score)

import numpy as np

a=[1, 4, 9, 16]
type(a)
sum(a)
dir(a)
mean(a)


x=np.array(a)
type(x)
sum(x)
dir(x)
x.var()
x.mean()

### 生成数据
np.arange(10)+1
np.arange(101, 201)
np.arange(101, 201, step=0.5)

np.linspace(101, 200, num=300)
np.linspace(1, 1, num=100)

np.random.seed(10)
np.random.randint(1, 10, size=20)
np.random.randint(1, 10, size=(5,3))

np.random.rand(100)
np.random.randn(100).var()

np.random.normal(2, 3, 100).var()


import pandas as pd
BSdata=pd.read_csv("./data/BSdata.csv", encoding="utf-8")
type(BSdata)

BSdata=pd.read_excel('./data/DaPy_data.xlsx', 1)

# dat=pd.read_clipboard()

del BSdata['学号']

BSdata.to_csv('./data/new.csv')
BSdata.to_excel('./data/new.xlsx')

BSdata=pd.read_excel('./data/DaPy_data.xlsx', 0)

BSdata.info()
BSdata.head()
BSdata.tail()
BSdata.head(10)
BSdata.tail(8)

BSdata.sort_values('支出', ascending=False)
BSdata.sort_index(axis=1, ascending=False)

BSdata.index
BSdata.columns
BSdata.values

BSdata.shape
BSdata.shape[0]
BSdata.shape[1]

import numpy as np
A=np.random.randint(0,10, size=(10, 5))
A.shape
A.reshape(25,2)

BSdata['体重指数']=BSdata.体重/(BSdata.身高/100)**2
BSdata.columns

BSdata.T
dir(BSdata)

B=np.random.randint(0,10, size=(10, 5))

A=pd.DataFrame(A)
B=pd.DataFrame(B)

pd.concat([A, B], axis=0)
pd.concat([A, B], axis=1)


#### 子集选取

### 选取单个变量
BSdata.info()
BSdata.支出

BSdata['支出']
BSdata[['支出','性别']]

BSdata[['学号','课程']]
BSdata.iloc[1,3]

BSdata.iloc[0:10,0:4]
BSdata.iloc[0:10,]

BSdata.iloc[:10,]
BSdata.iloc[[1,3,5],[1,3]]

type(BSdata)

BSdata.iloc[:10, ['性别', '支出']]
BSdata.loc[:10, ['性别', '支出']]

BSdata.iloc[:10,][['性别', '支出']]

BSdata[(BSdata.支出>40)&(BSdata.性别=='女')][['性别','支出']]

BSdata.loc[(BSdata.支出>40)&(BSdata.性别=='女'), ['性别','支出']]

import numpy as np

dat=np.random.randint(0,100, size=(50,8))
dat[[1,3,5], 3:7]
dat[[1,3,5], :7]

x=[1,4,9,12,39,14]
x[2:5]
x[[1,4]]

np.array(x)[[1,4]]

## if 语句
a=500

if a>100:
    print("数值大于100")
    print(a)

if a>100:
    print("数值大于100")
    print(a)
else:
    print("数值小于等于100")

print("数值大于100") if a>100 else print(a)

range(1,11)

import numpy as np
np.arange(1, 11)

for i in range(1, 11):
    print(i)

import string

string.ascii_lowercase
for i in string.ascii_lowercase:
    print(i)

for var in BSdata.columns:
    print(var)

x=np.random.randint(-10, 10, 15)

for i in x:
    if i>=0:
        print(i**0.5)
    else:
        break


for i in x:
    if i>=0:
        print(i**0.5)
    else:
        continue


y=[1,8,3, 19, 20, -4, 5,2,8,47]
type(y)

len(y)

sum(y)

def mean(Lst):
    return sum(Lst)/len(Lst)

mean(y)

y2=list()
for i in y:
    y2.append(i-1)



def ssq(Lst,x):
    res=list()
    for i in Lst:
        res.append((i-x)**2)
    return res

def var(Lst):
    """计算方差"""
    Lst_mean=mean(Lst)
    return sum(ssq(Lst,Lst_mean))/(len(Lst)-1)


var(y)

import numpy as np
np.var(y, ddof=1)

type(ssq)
type(y)

##### class

class Myclass:
    """第一个类"""
    i=1234
    def f(self):
        print('hello world')

a=Myclass()

type(a)
dir(a)
a.i
a.f()

class circle1:
    """一个二维平面中的圆"""
    pos=(0,0)
    r=1

class circle:
    """一个二维平面中的圆"""
    def __init__(self, t=(0,0), x=1):
        self.pos=t
        self.r=x
    def __str__(self):
        return print('圆：', '位置为：', self.pos, '半径为：', self.r)


b=circle1()
type(b)
dir(b)
b.pos
b.r

c=circle((1,1), 10)
c.pos
c.r

d=circle()
d.pos

g=circle((1,2), 20)
dir(g)
g.__doc__
g.__str__()
print(g)


import numpy as np
def c_area(x):
    return np.pi*x.r**2

c_area(g)

class circle:
    """一个二维平面中的圆"""
    def __init__(self, t=(0,0), x=1):
        self.pos=t
        self.r=x
    def __str__(self):
        return print('圆：', '位置为：', self.pos, '半径为：', self.r)
    def area(self):
        return np.pi*self.r**2
    def dis2(self, other):
        return ((self.pos[1]-other.pos[1])**2+(self.pos[0]-other.pos[0])**2)**0.5


h=circle((1,1), 4)
dir(h)
h.area()
type(h.area)
type(c_area)
type(h.pos)

k=circle((3,8), 3)

h.dis2(k)

