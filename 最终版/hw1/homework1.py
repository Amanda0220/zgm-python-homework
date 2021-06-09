### 作业内容
##  1. 分别创建一个列表,元组，字典，并提取其子集
x=[1,5,7,9,3]
x[2:4]
y=(1,5,7,9,3)
y[1:5]
z={'number':['20172000403','20172000409','20172000922'],'name':['Amanda','John','Horry'],'age':[20,20,19],'height':[162,178,172],'weight':[55,79,66]}
z['name']

##  2. 利用 numpy 生成一个一维数组和二维数组
import numpy as np
a=np.array([3,9,8,7,10,45,26])
b=np.array([[3,9,8,7,10,45,26],[9,0,7,6,335,467,58]])

##  3. 0-100之间生成等步长的201个数；把列表 [1,4,9] 重复10遍
c=np.linspace(0,100,201)
[1,4,9]*10

##  4. 随机生成8乘以20的整数array，并得到其转置数组，对其转置数组提取前10行，第2,5,8列数据
# np.random.seed(500)
d=np.random.randint(1,100,size=(8,20))
e=d.T
e[0:10,[1,4,7]]

##  5. 利用pandas把data文件夹中的 数据.xls 导入，要求使用相对路径
import pandas as pd
data=pd.read_excel('./data/数据.xls')

##  6. 显示 数据.xls 数据集的结构，前5条数据，后5条数据，所有变量名，及其维度
data.info()
data.head()
data.tail()
data.columns
data.shape

##  7. 对数据集增加一个变量HRsq，其为 HR数据的平方
data['HRsq']=(data.HR)**2

##  8. 对 数据.xls 数据集 进行子集的提取：
##     1. 删除有缺失值的年份
DS1=data.dropna()

##     2. 提取逢5，逢0年份的Year, GDP, KR, HRsq，CPI 变量的数据
DS2=data[data.Year % 5==0][['Year','GDP','KR','HRsq','CPI']]

##     3. 提取逢2，逢8年份的Year, GDP, KR, HRsq，CPI 变量的数据
DS3=data.loc[(data.Year % 10==2)|(data.Year % 10==8),['Year','GDP','KR','HRsq','CPI']]

##     4. 对2和3得到的数据集按行进行合并，并按年份进行排序
DS4=pd.concat([DS2,DS3],axis=0).sort_values(by='Year')

##     5. 提取1978年及之后的数据
DS5=data[data.Year>=1978]

##     6. 提取1978年之后且 KR 变量在 1~1.2之间的数据
DS6=data[(data.Year>=1978)&(data.KR>=1)&(data.KR<=1.2)]

##  9. 保存数据为csv和excel
##     1. 写出第8题中第4问得到的子集到data文件夹
DS4.to_csv("./data/8(4).csv")
DS4.to_excel("./data/8(4).xlsx")

##     2. 写出第8题中第6问得到的子集到data文件夹
DS6.to_csv("./data/8(6).csv")
DS6.to_excel("./data/8(6).xlsx")
