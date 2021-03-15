# -*- coding:utf-8 -*-
"""
Created on Mon Mar 15 13:52:09 2021

@author: lixiangwei
"""
from wordcloud import WordCloud
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('./Market_Basket_Optimisation.csv', header = None)

# make market information to str;
words = []
for i in range(0, data.shape[0]):
    temp = []
    for j in range(0, 20):
        if str(data.values[i, j]) != 'nan':
           temp.append(str(data.values[i, j]))
    words.append(temp)

s1 = ','.join(words[0])+','
for i in range(1, len(words)):
    s1 += ','.join(words[i])+','


wc = WordCloud(max_words=50, width=2000, height=1200)
wordcloud = wc.generate(s1)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

wordcloud.to_file("market_word_cloud.jpg")

