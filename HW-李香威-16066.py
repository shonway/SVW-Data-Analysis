# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 09:36:48 2021

@author: lixiangwei
"""

# =============================================================================
# HW1: accumulation of even numbers within 100
# =============================================================================
a = 0
for i in range(51):
    i = i*2
    print(i)
    a = a+i
print(a)


#%%
# =============================================================================
# HW2: statistic summary of grade
# =============================================================================
import pandas as pd

path = 'C:/Users/lixiangwei/Desktop/黑马/L1/car_data_analyze/grade.csv'
grade = pd.read_csv(path, header=0, encoding='gbk')

# statistic summary in total
print(grade.describe())

# add a new column for total grade
grade_num = grade.drop('姓名', axis=1)
grade['sum'] = grade_num.apply(lambda x: x.sum(), axis=1)
print(grade.describe())

# sort by total grade
grade = grade.sort_values('sum', ascending=False)
# reset index
grade = grade.reset_index()
grade = grade.drop('index', axis=1)

print(grade)
print('第1名是：', grade['姓名'][0], 'total grade is ', grade['sum'][0], '\n'
      '第2名是：', grade['姓名'][1], 'total grade is ', grade['sum'][1], '\n'
      '第3名是：', grade['姓名'][2], 'total grade is ', grade['sum'][2], '\n'
      '第4名是：', grade['姓名'][3], 'total grade is ', grade['sum'][3], '\n'
      '第5名是：', grade['姓名'][4], 'total grade is ', grade['sum'][4], '\n')

#%%
# =============================================================================
# HW3: car data analysis
# =============================================================================
path = 'C:/Users/lixiangwei/Desktop/黑马/L1/car_data_analyze/car_complain.csv'
car0 = pd.read_csv(path)

# take onehot key for problems 
issues = pd.get_dummies(car0['problem'], prefix='problem')
car1 = car0.join(issues)

# plot by brand, model, 
import seaborn as sns
sns.countplot(data=car0, y='brand', hue='car_model')
      

#%%
     
      
      
