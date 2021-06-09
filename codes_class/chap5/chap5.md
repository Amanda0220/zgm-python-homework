---
title: "第5章课程"
author: "邹格曼"
date: "2020年6月"
institute: 中南财经政法大学统计与数学学院
csl: ./style/chinese-gb7714-2015-numeric.csl
css: ./style/markdown.css
bibliography: [./Bibfile.bib]
eqnPrefixTemplate: ($$i$$)
link-citations: true
linkReferences: true
chapters: true
tableEqns: false
autoEqnLabels: false
classoption: "aspectratio=1610"
---





# 第5章代码

## 图形


```python
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
```

<img src="chap5_files/figure-html/unnamed-chunk-1-1.png" width="60%" style="display: block; margin: auto;" />


```python
BSdata=pd.read_csv("./data/BSdata.csv")
plt.scatter(BSdata.身高,BSdata.体重,s=BSdata.支出)
```

<img src="chap5_files/figure-html/unnamed-chunk-2-1.png" width="60%" style="display: block; margin: auto;" />

## 三维曲面

```python
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
```

<img src="chap5_files/figure-html/unnamed-chunk-3-1.png" width="60%" style="display: block; margin: auto;" />

## seaborn作图

```python
import seaborn as sns
```
### 箱线图（boxplot）

```python
sns.boxplot(BSdata.身高)
```

<img src="chap5_files/figure-html/unnamed-chunk-5-1.png" width="60%" style="display: block; margin: auto;" />

```python
plt.boxplot(BSdata.身高)
```

```python
sns.boxplot(y=BSdata.身高)
```

<img src="chap5_files/figure-html/unnamed-chunk-7-1.png" width="60%" style="display: block; margin: auto;" />

```python
sns.boxplot(x=BSdata.性别,y=BSdata.身高)
```

<img src="chap5_files/figure-html/unnamed-chunk-8-1.png" width="60%" style="display: block; margin: auto;" />

```python
sns.boxplot(y=BSdata.开设,x=BSdata.支出,hue=BSdata.性别)
plt.text(80,1,r'$\bar x$')
```

<img src="chap5_files/figure-html/unnamed-chunk-9-1.png" width="60%" style="display: block; margin: auto;" />

### 小提琴图（xiolinplot）

```python
sns.violinplot(x='性别',y='身高',data=BSdata)
```

<img src="chap5_files/figure-html/unnamed-chunk-10-1.png" width="60%" style="display: block; margin: auto;" />

```python
sns.violinplot(x='开设', y='支出',hue='性别',data=BSdata)
```

<img src="chap5_files/figure-html/unnamed-chunk-11-1.png" width="60%" style="display: block; margin: auto;" />
### 点图（stripplot）

```python
sns.stripplot(x='性别', y='身高',data=BSdata)
```

<img src="chap5_files/figure-html/unnamed-chunk-12-1.png" width="60%" style="display: block; margin: auto;" />

```python
sns.stripplot(x='性别', y='身高',data=BSdata,jitter=True)
```

<img src="chap5_files/figure-html/unnamed-chunk-13-1.png" width="60%" style="display: block; margin: auto;" />

```python
sns.stripplot(y='性别', x='身高',data=BSdata,jitter=True)
```

<img src="chap5_files/figure-html/unnamed-chunk-14-1.png" width="60%" style="display: block; margin: auto;" />

### 条图（barplot）

```python
sns.barplot(x='性别', y='身高',data=BSdata,ci=0,palette="Blues_d")
```

<img src="chap5_files/figure-html/unnamed-chunk-15-1.png" width="60%" style="display: block; margin: auto;" />

### 计数图（countplot）

```python
sns.countplot(x='性别',data=BSdata)
```

<img src="chap5_files/figure-html/unnamed-chunk-16-1.png" width="60%" style="display: block; margin: auto;" />

```python
sns.countplot(y='开设',data=BSdata)
```

<img src="chap5_files/figure-html/unnamed-chunk-17-1.png" width="60%" style="display: block; margin: auto;" />

```python
sns.countplot(x='性别',hue='开设',data=BSdata)
```

<img src="chap5_files/figure-html/unnamed-chunk-18-1.png" width="60%" style="display: block; margin: auto;" />

### 分组关系图（catplot）

```python
sns.catplot(x='性别',col='开设', col_wrap=3,data=BSdata,kind='count',height=2.5, aspect=.8)
```

```python
sns.distplot(BSdata['身高'],kde=True,bins=20,rug=True)
```

<img src="chap5_files/figure-html/unnamed-chunk-20-1.png" width="60%" style="display: block; margin: auto;" />

```python
sns.jointplot(x='身高', y='体重', data=BSdata)
```

```python
sns.pairplot(BSdata[['身高','体重','支出']])
```

## ggplot绘图系统

```python
from ggplot import *
qplot('身高',data=BSdata, geom='histogram')
```

<img src="chap5_files/figure-html/unnamed-chunk-23-1.png" width="60%" style="display: block; margin: auto;" />

```python
qplot('身高','体重',data=BSdata,color='性别')
```

<img src="chap5_files/figure-html/unnamed-chunk-23-2.png" width="60%" style="display: block; margin: auto;" />

```python
GP=ggplot(aes(x='身高',y='体重'),data=BSdata) #绘制直角坐标系
GP+geom_point()+geom_line() #不同图层可以用'+'叠加
```

<img src="chap5_files/figure-html/unnamed-chunk-23-3.png" width="60%" style="display: block; margin: auto;" />

```python
GP+geom_point()+facet_wrap('性别') #facet_wrap是分类变量
```

<img src="chap5_files/figure-html/unnamed-chunk-23-4.png" width="60%" style="display: block; margin: auto;" />

```python
GP+geom_point()+facet_wrap('性别',nrow=1,ncol=2)
```

<img src="chap5_files/figure-html/unnamed-chunk-23-5.png" width="60%" style="display: block; margin: auto;" />

```python
GP+geom_point()+facet_wrap('性别',nrow=1,ncol=2)+theme_xkcd()
```

<img src="chap5_files/figure-html/unnamed-chunk-23-6.png" width="60%" style="display: block; margin: auto;" />

## 公式
样本均值$\bar x$的计算公式为：
$$\bar x=\frac{1}{n}\sum_i^n x_i$$
$\alpha$


# 参考文献
[//]: # (\bibliography{Bibfile})
