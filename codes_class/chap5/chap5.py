import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimSun']

x=np.linspace(-4*math.pi,4*math.pi,101)

plt.plot(x,np.sin(x))
plt.plot(x,np.cos(x))
plt.plot(x,np.log(x))
plt.text(6,-30,'$y=\log(x)+\sum_{i=1}^n x_i$')

BSdata=pd.read_csv("./data/BSdata.csv")
plt.scatter(BSdata.身高,BSdata.体重,s=BSdata.支出)

from mpl_toolkits.mplot3d import Axes3D

x=y=np.linspace(-4,4,21)
X,Y=np.meshgrid(x,y)
Z=np.sqrt(X**2+Y**2)

fig1=plt.figure()
ax1=Axes3D(fig1)
ax1.plot_surface(X,Y,Z)

fig2=plt.figure()
ax2=Axes3D(fig2)
ax2.scatter(X,Y,Z)

fig3=plt.figure()
ax3=Axes3D(fig3)
ax3.scatter(BSdata.身高,BSdata.体重,s=50*np.random.rand(1))

import seaborn as sns

sns.boxplot(BSdata.身高)
plt.boxplot(BSdata.身高)
sns.boxplot(y=BSdata.身高)
sns.boxplot(x=BSdata.性别,y=BSdata.身高)
sns.boxplot(y=BSdata.开设,x=BSdata.支出,hue=BSdata.性别)
plt.text(80,1,r'$\bar x$')

sns.violinplot(x='性别',y='身高',data=BSdata)
sns.violinplot(x='开设', y='支出',hue='性别',data=BSdata)

sns.stripplot(x='性别', y='身高',data=BSdata)
sns.stripplot(x='性别', y='身高',data=BSdata,jitter=True)
sns.stripplot(y='性别', x='身高',data=BSdata,jitter=True)

sns.barplot(x='性别', y='身高',data=BSdata,ci=0,palette="Blues_d")

sns.countplot(x='性别',data=BSdata)
sns.countplot(y='开设',data=BSdata)
sns.countplot(x='性别',hue='开设',data=BSdata)

sns.catplot(x='性别',col='开设', col_wrap=3,data=BSdata,kind='count',height=2.5, aspect=.8)
sns.distplot(BSdata['身高'],kde=True,bins=20,rug=True)
sns.jointplot(x='身高', y='体重', data=BSdata)
sns.pairplot(BSdata[['身高','体重','支出']])

from ggplot import *
qplot('身高',data=BSdata, geom='histogram')
qplot('身高','体重',data=BSdata,color='性别')

GP=ggplot(aes(x='身高',y='体重'),data=BSdata) #绘制直角坐标系
GP+geom_point()+geom_line() #不同图层可以用'+'叠加

GP+geom_point()+facet_wrap('性别') #facet_wrap是分类变量
GP+geom_point()+facet_wrap('性别',nrow=1,ncol=2)
GP+geom_point()+facet_wrap('性别',nrow=1,ncol=2)+theme_xkcd()
