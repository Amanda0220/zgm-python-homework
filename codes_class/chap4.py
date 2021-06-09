###############20200430###################
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# plt.rcParams['font.sans-serif']=['SimSun'] #作图字体为宋体
plt.rcParams['font.sans-serif']=['KaiTi'] #作图字体为楷体
plt.rcParams['axes.unicode_minus']=False #正确显示负号

BSdata=pd.read_excel('./data/DaPy_data.xlsx')
dir(BSdata)
BSdata.columns
BSdata.index
BSdata.describe()
BSdata[['性别','开设','课程','软件']].describe()
BSdata[['性别','开设','身高','课程','软件']].describe() #若包含数值型数据，描述仅出现数值型数据

BSdata.课程.value_counts()
BSdata.支出.var()
BSdata.支出.quantile() #默认中位数
BSdata.支出.quantile(0.25)
BSdata.支出.quantile(0.75)
BSdata.支出.quantile([0.25,0.5,0.75])

IQR=BSdata.身高.quantile(0.75)-BSdata.身高.quantile(0.25);IQR

T1=BSdata.性别.value_counts();T1
T1/sum(T1)*100  #频数统计分析

#求百分位点
fre=np.arange(0.1,1,0.01)
BSdata.支出.quantile(fre)

BSdata.支出.skew() #偏度
BSdata.支出.kurt() #峰度

#自编统计函数
def stats(x):
    stat=[x.count(),x.min(),x.quantile(0.25),x.mean(),x.median(),x.quantile(0.75),x.max(),x.max()-x.min(),x.var(),x.std(),x.skew(),x.kurt()]
    stat=pd.Series(stat,index=['Count','Min', 'Q1(25%)','Mean','Median','Q3(75%)','Max','Range','Var','Std','Skew','Kurt'])
    return(stat)
stats(BSdata.身高)
BSdata.身高.describe()


BSdata[['身高','体重']].mean()
BSdata[['身高','体重']].var()
BSdata[['身高','体重']].cov() #协方差矩阵
BSdata[['身高','体重']].corr() #相关系数矩阵

res=BSdata.课程.value_counts()
Y=res.values
X=res.index
plt.bar(X,Y)  #记得输入字体
plt.barh(X,Y)  #横向条形图
res.plot(kind='bar') #做条形图，命令作用同plt.bar()

###############20200507###################
# 饼图
plt.pie(Y,labels=X) #记得敲参数
res.plot(kind='pie') #不需要提取XY的值

# 直方图
plt.plot(BSdata.身高) #画出身高的线图
plt.hist(BSdata.身高) #直方图
plt.hist(BSdata.身高,density=True) #直方图,以频率作图

# 散点图
plt.scatter(BSdata.身高,BSdata.体重) # 散点图
plt.ylim(40,100) #需要与上一行一起运行

# 图形参数设置
plt.plot(BSdata.身高,'rv--') #red,v下三角,--虚线(顺序可调整)
plt.plot(BSdata.身高,color="red",linestyle='--',marker='s') #red,s正方形,--虚线

# 低级绘图命令
plt.plot(BSdata.身高,'rv--') #red,v下三角,--虚线(顺序可调整)
plt.plot(BSdata.身高,'rv--',label='身高')
plt.axhline(170) #水平线
plt.axvline(20) #垂直线
plt.axhspan(165,175) #水平带

plt.text(35,185,"maximum") #在（35,185）位置,添加文本“maximum”

plt.plot(BSdata.身高,'rv:',label='身高')
plt.legend() #产生图例,注意作图时要有label,才能给图例命名

# 多图
plt.figure(figsize=(12,6)) #画布,(12,6)长12英寸,宽6英寸
plt.subplot(1,2,1);plt.bar(X,Y)
# plt.subplot(121);plt.bar(X,Y)
plt.subplot(1,2,2);plt.pie(Y,labels=X)
# plt.subplot(122);plt.pie(Y,labels=X) #字图形不超过9，可简写

# 简写
plt.figure(figsize=(12,6))
plt.subplot(241);res.plot(kind='bar')
plt.subplot(242);res.plot(kind='pie')
plt.subplot(243);res.plot(kind='bar')
plt.subplot(244);res.plot(kind='pie')
plt.subplot(245);res.plot(kind='bar')
plt.subplot(246);res.plot(kind='pie')
plt.subplot(247);res.plot(kind='bar')
plt.subplot(248);res.plot(kind='pie')

plt.subplots(2,4,figsize=(12,6)) #同时做了画布和分割

fig,ax=plt.subplots(2,4,figsize=(12,6))
ax[0,0].bar(X,Y)
ax[0,1].plot(BSdata.身高)
ax[0,2].bar(X,Y)
ax[0,3].plot(BSdata.身高)
ax[1,0].bar(X,Y)
ax[1,1].plot(BSdata.身高)
ax[1,2].bar(X,Y)
ax[1,3].plot(BSdata.身高)
fig.set_facecolor('red') #画布颜色设置为红
ax[0,0].set_title('第一个图')

# 基于Pandas的绘图
BSdata.plot(kind='scatter',x='身高',y='体重')

# 一维频数分析
pd.cut(BSdata.身高,bins=10).value_counts()
pd.cut(BSdata.身高,bins=[0,155,160,165,170,175,180,250])
x=pd.cut(BSdata.身高,bins=[0,155,160,165,170,175,180,250])
x.value_counts(sort=False).plot(kind='pie')

# 二维数据分析
pd.crosstab(BSdata.开设,BSdata.课程)
pd.crosstab(BSdata.开设,BSdata.课程,margins=True,margins_name='小计')
pd.crosstab(BSdata.开设,BSdata.课程,margins=True,margins_name='小计',normalize="all")
pd.crosstab(BSdata.开设,BSdata.课程,margins=True,margins_name='小计',normalize="index") #对行求百分比
pd.crosstab(BSdata.开设,BSdata.课程,margins=True,margins_name='小计',normalize="columns") #对列求百分比
pd.crosstab(BSdata.开设,BSdata.课程,margins=True,normalize='all').round(3) #round保留3位小数

# 复式条图
pd.crosstab(BSdata.开设,BSdata.课程).plot(kind='bar')
pd.crosstab(BSdata.开设,BSdata.性别).plot(kind='bar')
pd.crosstab(BSdata.性别,BSdata.开设).plot(kind='bar')

# 分组
BSdata.groupby(['性别'])
BSdata.groupby(['性别'])['身高'].mean()
BSdata.groupby(['性别'])['身高'].size()
BSdata.groupby(['性别','开设'])['身高'].mean()

pd.crosstab(BSdata.性别,BSdata.开设)
BSdata.groupby(['性别','开设']).count()
BSdata.groupby(['性别','开设']).size()

BSdata.groupby(['性别'])['体重'].agg([np.mean, np.std])
BSdata.groupby(['性别'])['身高','体重'].agg({'身高':np.var,'体重':np.std})


#######################20200514#######################
# 定性数据透视分析
BSdata.pivot_table(index=['性别'],values=['学号'],aggfunc=len)
BSdata.pivot_table(index=['开设'],values=['课程'],aggfunc=len)
BSdata.pivot_table(index=['开设'],values=['性别'],aggfunc=len)

BSdata.pivot_table(index=['开设','性别'],values=['课程'],aggfunc=len)
BSdata.pivot_table(index=['开设','性别'],values=['软件'],aggfunc=len)

BSdata.pivot_table(index=['开设','性别'],values=['身高'],aggfunc=np.mean)
BSdata.pivot_table(index=['开设','性别'],values=['体重'],aggfunc=np.mean)
BSdata.pivot_table(index=['开设','性别'],values=['身高','体重'],aggfunc=[np.mean,np.var])
BSdata.pivot_table(index=['开设','性别'],values=['身高','体重'],aggfunc={'身高':np.mean,'体重':np.var})
BSdata.pivot_table(index=['开设','性别'],values=['身高','体重'],margins=True,margins_name='合计',aggfunc={'身高':np.mean,'体重':np.var})

### DataFrame Apply 方法
BSdata[['身高','体重','支出']].mean()
BSdata[['身高','体重','支出']].apply(np.mean,axis=1) #按照行求平均值
BSdata[['身高','体重','支出']].apply(np.var,axis=1) #按照行求方差
BSdata[['身高','体重','支出']].apply([np.mean,np.var],axis=1)
BSdata[['身高','体重','支出']].apply({'身高':np.mean,'体重':np.var}) 
BSdata.groupby('性别')['身高','体重'].mean()

BSdata.groupby(['性别'])['身高','体重'].apply(np.mean)
BSdata.groupby(['性别'])[['身高','体重','支出']].apply(np.mean,axis=1)

#######################20200521#######################




