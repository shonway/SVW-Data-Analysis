"""
赛题1：汽车用户情感分析可视化
"""
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('C:/Users/lixiangwei/Desktop/2021数据黑马训练营结营考试（L1认证）/赛题1./train.csv')
data['sentiment_word'].fillna('无', inplace = True)
print(data)
print(data.shape)

#%%
# =============================================================================
# 情感词云可视化;
# =============================================================================
words = []   
for i in range(0, data.shape[0]):
    temp = []
    if str(data.values[i, 4]) != 'nan':
        temp.append(str(data.values[i, 4]))
    words.append(temp)   

# drop empty;
# words = [i for i in words if i != []]

s1 = ','.join(words[0])+','
for i in range(1, len(words)):
    s1 += ','.join(words[i])+','

# =============================================================================
# WordCloud需配置中文字体库; 
# refer to: https://blog.csdn.net/Dick633/article/details/80261233
# =============================================================================
wc = WordCloud(max_words=50, width=2000, height=1200)
wordcloud = wc.generate(s1)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
wordcloud.to_file("情感词云.jpg")

#%%
# =============================================================================
# 主题-情感-情感词柱状图可视化;
# =============================================================================
# assign x_axis with diffent subjects;
x_axis = data['subject'].value_counts().index.tolist()

# assign labels with different sentiment values;
labels = data['sentiment_value'].value_counts().index.tolist()

# assign y_axis with amount of different sentiment values among each subject;
y = []
for i in x_axis:
    y.append(data[data.subject == i])

# classification of y;
y_neural = []
y_positive = []
y_negative = []
for i in range(len(x_axis)):
    y_neural.append(y[i]['sentiment_value'].value_counts()[0]) 
    y_positive.append(y[i]['sentiment_value'].value_counts()[1])
    y_negative.append(y[i]['sentiment_value'].value_counts()[-1])

# bar plot; 
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.bar(x_axis, y_negative, label = 'negative attitude', fc = 'r')
plt.bar(x_axis, y_neural, label = 'neural attitude', fc = 'y', bottom = y_negative)
plt.bar(x_axis, y_positive, label = 'positive attitude', bottom = y_neural, fc = 'b')
plt.tick_params(direction='out',labelsize=12,length=5.5,width=1,top=False,right=False)
plt.legend()
plt.show()

#%%
# =============================================================================
# 热力图关联性分析
# =============================================================================
# numerize and regulize catagorical features;
from sklearn.preprocessing import LabelEncoder
import numpy as np
import seaborn as sn
le = LabelEncoder()
data['subject'] = le.fit_transform(data['subject'])
data['sentiment_word'] = le.fit_transform(data['sentiment_word'])

# heatmap
corrMatt = data.corr()
mask = np.array(corrMatt)
mask[np.tril_indices_from(mask)] = False
fig,ax= plt.subplots()
fig.set_size_inches(20,10)
sn.heatmap(corrMatt, mask=mask,vmax=.8, square=True,annot=True)


