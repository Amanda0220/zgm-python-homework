---
title: "第5章代码"
author: "Jin"
date: "2020年3月"
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

## 特殊统计图的绘制

### 函数图像


```python
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimSun']

x=np.linspace(-4*math.pi, 4*math.pi, 101)

plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
plt.plot(x, np.log(x))
plt.text(6, -30, '$y=\log(x)+\sum_{i=1}^n x_i$')
```

<div class="figure" style="text-align: center">
<img src="c:/Works/Teaching/2020年上半年--Python数据分析/codes/chap5/chap5_files/figure-html/unnamed-chunk-1-1.png" alt="函数图像" width="60%" />
<p class="caption">(\#fig:unnamed-chunk-1)函数图像</p>
</div>


```python
BSdata=pd.read_csv('./data/BSdata.csv')
plt.scatter(BSdata.身高, BSdata.体重, s=BSdata.支出)
```

<div class="figure" style="text-align: center">
<img src="c:/Works/Teaching/2020年上半年--Python数据分析/codes/chap5/chap5_files/figure-html/unnamed-chunk-2-1.png" alt="气泡图" width="60%" />
<p class="caption">(\#fig:unnamed-chunk-2)气泡图</p>
</div>

### 三维曲面


```python
from mpl_toolkits.mplot3d import Axes3D

x=y=np.linspace(-4, 4, 21)
X,Y=np.meshgrid(x,y)
Z=np.sqrt(X**2+Y**2)

fig1=plt.figure()
ax1=Axes3D(fig1)
ax1.plot_surface(X,Y,Z)

fig2=plt.figure()
ax2=Axes3D(fig2)
ax2.scatter(BSdata.身高, BSdata.体重, BSdata.支出, s=50*np.random.rand(52))
```

<img src="c:/Works/Teaching/2020年上半年--Python数据分析/codes/chap5/chap5_files/figure-html/unnamed-chunk-3-1.png" width="60%" style="display: block; margin: auto;" />

## seaborn 作图


```python
import seaborn as sns
sns.boxplot(BSdata.身高)
plt.boxplot(BSdata.身高)
```

```python
sns.boxplot(y=BSdata.身高)
sns.boxplot(x=BSdata.性别,y=BSdata.身高)
```

```python
sns.boxplot(y=BSdata.开设, x=BSdata.支出, hue=BSdata.性别)
```

```python
plt.text(80,1,r'$\bar x$')

sns.violinplot(x='性别', y='身高',data=BSdata)
sns.violinplot(x='开设', y='支出',hue='性别',data=BSdata)
```

```python
sns.stripplot(x='性别', y='身高',data=BSdata)
```

```python
sns.stripplot(x='性别', y='身高',data=BSdata,jitter=True)
```

```python
sns.stripplot(y='性别', x='身高',data=BSdata,jitter=True)
```

```python
sns.barplot(x='性别', y='身高',data=BSdata,ci=0,palette='Blues_d')

```

```python
sns.countplot(x='性别',data=BSdata)
```

```python
sns.countplot(y='开设',data=BSdata)
```

```python
sns.countplot(x='性别',hue='开设',data=BSdata)
```


```python
sns.catplot(x='性别',col='开设', col_wrap=3,data=BSdata, kind='count',height=2.5, aspect=.8)
```

```python
plt.show()
```

<img src="c:/Works/Teaching/2020年上半年--Python数据分析/codes/chap5/chap5_files/figure-html/unnamed-chunk-5-1.png" width="60%" style="display: block; margin: auto;" />

样本均值 $\bar x$ 的计算公式为：
$$\bar x=\frac{1}{n}\sum_i^n x_i$$



# 参考文献
[//]: # (\bibliography{Bibfile})
