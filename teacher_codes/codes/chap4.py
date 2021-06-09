import numpy as np
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimSun']

BSdata=pd.read_csv('./data/BSdata.csv')

dir(BSdata)

BSdata.columns
BSdata.describe()

BSdata[['性别','开设','课程','软件']].describe()
BSdata.课程.value_counts()

BSdata.支出.var()
BSdata.支出.quantile([0.25, 0.5, 0.75])

BSdata.支出.quantile(np.arange(0.01,1, 0.01))

BSdata.支出.skew()
BSdata.支出.kurt()

BSdata[['身高', '体重']].mean()
BSdata[['身高', '体重']].var()
BSdata[['身高', '体重']].cov()
BSdata[['身高', '体重']].corr()


res=BSdata.课程.value_counts()

Y=res.values
X=res.index

plt.bar(X, Y)
plt.barh(X, Y)

res.plot(kind='bar')
res.plot(kind='barh')

## 饼图
plt.pie(Y, labels=X)

res.plot(kind='pie')

BSdata.columns

plt.plot(BSdata.身高)
plt.hist(BSdata.身高)
plt.hist(BSdata.身高, density=True)

plt.scatter(BSdata.身高, BSdata.体重)
plt.ylim(40, 100)

plt.plot(BSdata.身高, 'rv--', label=u'身高')
plt.plot(BSdata.身高, color='r', marker='v', linestyle='--')
plt.axhline(170)
plt.axvline(20)
plt.axhspan(165, 175)
plt.text(35, 185, '最大值')
plt.legend()


## 多图
plt.figure(figsize=(12,6))
plt.subplot(1,2,1); res.plot(kind='bar')
plt.subplot(1,2,2); res.plot(kind='pie')

## 简写
plt.figure(figsize=(12,6))
plt.subplot(121); res.plot(kind='bar')
plt.subplot(122); res.plot(kind='pie')

plt.figure(figsize=(12,6))
plt.subplot(241); res.plot(kind='bar')
plt.subplot(242); res.plot(kind='pie')
plt.subplot(243); res.plot(kind='bar')
plt.subplot(244); res.plot(kind='pie')
plt.subplot(245); res.plot(kind='bar')
plt.subplot(246); res.plot(kind='pie')
plt.subplot(247); res.plot(kind='bar')
plt.subplot(248); res.plot(kind='pie')

fig, ax=plt.subplots(2,4, figsize=(12,6))
ax[0,0].bar(X,Y)
ax[0,1].plot(BSdata.身高)
ax[0,2].bar(X,Y)
ax[0,2].plot(BSdata.身高)
ax[1,0].bar(X,Y)
ax[1,1].plot(BSdata.身高)
ax[1,2].bar(X,Y)
ax[1,3].plot(BSdata.身高)
fig.set_facecolor('red')
ax[0,0].set_title('第一个图')

BSdata.plot(kind='scatter', x='身高', y='体重')

pd.cut(BSdata.身高, bins=10)
x=pd.cut(BSdata.身高, bins=[0,155, 160, 165, 170, 175, 180,250])
x.value_counts(sort=False).plot(kind='pie')

BSdata.columns
pd.crosstab(BSdata.开设, BSdata.课程).plot(kind='bar')
pd.crosstab(BSdata.开设, BSdata.课程, margins=True,margins_name='小计')
pd.crosstab(BSdata.开设, BSdata.课程, margins=True,margins_name='小计', normalize='all')
pd.crosstab(BSdata.开设, BSdata.课程, margins=True,margins_name='小计', normalize='index')
pd.crosstab(BSdata.开设, BSdata.课程, margins=True,margins_name='小计', normalize='columns')
pd.crosstab(BSdata.开设, BSdata.课程, margins=True,margins_name='小计', normalize='columns').round(3)

pd.crosstab(BSdata.开设, BSdata.性别).plot(kind='bar')
pd.crosstab(BSdata.性别, BSdata.开设).plot(kind='bar')

BSdata.groupby(['性别'])['身高'].mean()
BSdata.groupby(['性别'])['身高'].var()

BSdata.groupby(['性别', '开设'])['身高'].mean()
pd.crosstab(BSdata.性别, BSdata.开设)
BSdata.groupby(['性别', '开设']).count()
BSdata.groupby(['性别', '开设']).size()

BSdata.groupby(['性别'])['身高'].mean()
BSdata.groupby(['性别'])['身高'].var()
BSdata.groupby(['性别'])['身高'].std()

BSdata.groupby(['性别'])['身高'].agg([np.mean, np.var, np.std])

BSdata.groupby(['性别'])[['身高','体重']].agg({'身高':np.var, '体重':np.std})
BSdata.groupby(['性别'])[['身高','体重']].apply(np.var)
BSdata.groupby(['性别'])[['身高','体重']].agg(np.var)
BSdata.groupby(['性别'])[['身高','体重']].var(ddof=0)
BSdata.groupby(['性别'])['身高','体重'].apply(np.var)
BSdata.groupby(['性别'])['身高','体重'].agg(np.var)
BSdata.groupby(['性别'])['身高','体重'].var()
BSdata.groupby(['性别'])['身高','体重'].agg(len)

BSdata.groupby(['性别'])[['身高','体重']].apply(sum)
BSdata.groupby(['性别'])[['身高','体重']].agg([sum], axis=0)

BSdata.groupby(['性别'])[['身高','体重']].apply(lambda x:print(x))
BSdata.groupby(['性别'])[['身高','体重']].agg(lambda x:print(x))

BSdata.groupby(['性别'])[['身高','体重']].apply(lambda x:np.sum(x.values))
BSdata.groupby(['性别'])[['身高','体重']].agg(lambda x:np.sum(x.values))

BSdata[['身高','体重']].agg([np.sum,np.var], axis=1)

np.var([1,2,3], ddof=1)
pd.DataFrame([1,2,3]).var()
pd.DataFrame([1,2,3]).apply(np.var)
pd.DataFrame([1,2,3]).agg(np.var)


BSdata.pivot_table(index=['性别'], values=['开设'], aggfunc=len)

BSdata.pivot_table(index=['开设'], values=['课程'], aggfunc=len)
BSdata.pivot_table(index=['开设'], values=['性别'], aggfunc=len)


BSdata.pivot_table(index=['开设', '性别'], values=['课程'], aggfunc=len)
BSdata.pivot_table(index=['开设', '性别'], values=['软件'], aggfunc=len)

BSdata.pivot_table(index=['开设', '性别'], values=['身高'], aggfunc=np.mean)
BSdata.pivot_table(index=['开设', '性别'], values=['体重'], aggfunc=np.mean)
BSdata.pivot_table(index=['开设', '性别'], values=['身高', '体重'], aggfunc=[np.mean, np.var])
BSdata.pivot_table(index=['开设', '性别'], values=['身高', '体重'], aggfunc={'身高':np.mean, '体重':np.var})
BSdata.pivot_table(index=['开设', '性别'], values=['身高', '体重'], margins=True, margins_name='合计',aggfunc={'身高':np.mean, '体重':np.var})

### Dataframe Apply 方法
BSdata[['身高', '体重', '支出']].mean()
BSdata[['身高', '体重', '支出']].apply(np.mean, axis=1)
BSdata[['身高', '体重', '支出']].apply(np.var, axis=1)
BSdata[['身高', '体重', '支出']].apply([np.mean,np.var], axis=1)

BSdata.groupby('性别')[['身高', '体重']].mean()

