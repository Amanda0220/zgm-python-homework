# 使用在校生数据集，利用python代码回答：
#  1. 该校男生，女生分布有多少人
import numpy as np
import pandas as pd
students=pd.read_excel("./data/在校生.xls")

students.性别.value_counts()

#  2. 该校各个省分别有多少人
students.生源所在地.value_counts()

#  3. 该校各个省各个民族分别有多少人，分别所占的百分比是多少，并给出行列合计，结果写为csv
## 各省各民族人数
count1=pd.crosstab(students.生源所在地,students.民族,margins=True,margins_name='合计')
count1
count1.to_csv('./ProvinceNation.csv',encoding='gbk')

## 各省各民族所占百分比
count2=pd.crosstab(students.生源所在地,students.民族,margins=True,margins_name='合计',normalize="all")
count2
count2.to_csv('./PProvinceNation.csv',encoding='gbk')

#  4. 该校各个专业，各个省，男女分别有多少人，结果写为csv
count3=pd.crosstab([students.专业,students.生源所在地],students.性别)
count3
count3.to_csv('./MajorProvinceGender.csv',encoding='gbk')


#  5. 各个专业的三门课平均成绩是多少，方差是多少
dtset1=students.pivot_table(index='专业', values=['分数1','分数2','分数3'], aggfunc=[np.mean,np.var])
dtset1

#  6. 各个专业所有课的整体平均分和方差是多少
# dtset1['mean'].apply([np.mean,np.var],axis=1) 错了

mean_all=lambda z:np.mean(z.values)
var_all=lambda z:np.var(z.values)
students_mean_all=students.groupby('专业')[['分数1','分数2','分数3']].apply(mean_all)
students_var_all=students.groupby('专业')[['分数1','分数2','分数3']].apply(var_all)
dtset2=pd.concat([students_mean_all,students_var_all],axis=1)
dtset2.columns=['mean','var']
dtset2

#  7. 每个学生的平均分和方差是多少
dtset3=students[['分数1','分数2','分数3']].agg([np.mean,np.var],axis=1);dtset3

#  8. 所有学生的平均分和方差
x=students[['分数1','分数2','分数3']]
xmean=np.mean(x.values);xmean
xvar=np.var(x.values);xvar

#  9. 各个专业男女生的三门课平均分在80分以上的有多少人
## 计算每人三门课的平均分
students['scoremean']=students[['分数1','分数2','分数3']].mean(axis=1)
## 筛选平均分在80以上的数据
abv=students[(students.scoremean>=80)]
## 统计
pd.crosstab(abv.专业,abv.性别)

#  10. 找出 '学生成绩单' sheet中学生的所有其他信息，并合并到其中，把结果写为csv(使用pd的 merge 或 join 方法)
score=pd.read_excel('./data/在校生.xls','学生成绩单')
del students['scoremean']
alldata=pd.merge(students,score,on='学号')
# alldata=pd.merge(students,score) 没有指明‘学号’也行
alldata
alldata.to_csv('./alldata.csv',encoding='gbk')

#  11. 计算合并后数据集中6门课成绩的平均分，中位数，方差，标准差，四分位点，百分位点，峰度和偏度
scoreall=alldata[['分数1','分数2','分数3','分数4','分数5','分数6']]
# 平均分
scoreall.mean()
# 中位数
scoreall.median()
# 方差
scoreall.var()
# 标准差
scoreall.std()
# 四分位点
scoreall.quantile([0.25,0.5,0.75])
# 百分位点
fre=np.arange(0.1,1,0.01)
scoreall.quantile(fre)
# 峰度
scoreall.kurt()
# 偏度
scoreall.skew()