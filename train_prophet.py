# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 10:39:59 2021

Time-series prediction model by prophet;

@author: lixiangwei
"""

import pandas as pd
from fbprophet import Prophet
import matplotlib.pyplot as plt

df = pd.read_csv('train.csv')
df.rename(columns = {'Datetime':'ds', 'Count':'y'}, inplace = True)

df = df.drop('ID', axis=1)

print(df.head())

#%%
# fitting model;
model = Prophet()
model.fit(df)

# prediction for upcoming 7 months by days;
future = model.make_future_dataframe(periods = 210)
print(future.tail())

forecast = model.predict(future)
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())

# plot out prediction;
model.plot(forecast)
plt.show()

model.plot_components(forecast)
print(forecast.columns)

