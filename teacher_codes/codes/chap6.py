## N(1, 3^2)  P{2<X<5}
import numpy as np
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt


rv1=stats.norm(1, 3)
rv1.mean()

rv1.cdf(5)-rv1.cdf(2)

rv1.ppf(0.975)

rv1.pdf(2)

xs=np.linspace(-10, 12, num=101)

plt.plot(xs, rv1.pdf(xs))

np.random.normal(1, 3, 100)
rv1.rvs(100)

rv1.stats()
rv1.std()
rv1.var()

rv2=stats.t(10) 
rv2.mean()

rv2.cdf(5)-rv2.cdf(2)

rv2.ppf(0.975)

rv2.pdf(2)

xs=np.linspace(-10, 12, num=101)

plt.plot(xs, rv2.pdf(xs))

np.random.standard_t(10, 100)

stats.norm.ppf(0.975, 1, 3)

BSdata=pd.read_csv('./data/BSdata.csv')
BSdata.columns

BSdata.身高.mean()-stats.norm.ppf(0.975)*BSdata.身高.std()/np.sqrt(BSdata.shape[0])
BSdata.身高.mean()+stats.norm.ppf(0.975)*BSdata.身高.std()/np.sqrt(BSdata.shape[0])


Z0=(BSdata.体重.mean()-70)/(BSdata.体重.std()/np.sqrt(BSdata.shape[0]))

alpha=0.05

(1-stats.norm.cdf(abs(Z0)))*2

def norm_u_test(X, u0):
    n=len(X)
    Z0=(np.mean(X)-u0)/(np.std(X, ddof=1)/n**0.5)
    if n>=30:
        P=(1-stats.norm.cdf(abs(Z0)))*2
    else:
        P=(1-stats.t.cdf(abs(Z0), (n-1)))*2     
    return P

norm_u_test(BSdata.体重, 70)

##### 线性回归
trees=pd.read_csv('./data/trees.csv')

import statsmodels.api as sm
import statsmodels.formula.api as smf

mod=smf.ols('Volume~Girth+Height', data=trees)
res=mod.fit()
res.summary()