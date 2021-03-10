import pandas as pd

from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

# header=None，不将第一行作为head
data = pd.read_csv('./Market_Basket_Optimisation.csv', header = None) 


# 将数据存放到transactions中
transactions = []
for i in range(0, data.shape[0]):
    temp = []
    for j in range(0, 20):
        if str(data.values[i, j]) != 'nan':
           temp.append(str(data.values[i, j]))
    transactions.append(temp)


#%%
# make a new dataframe including transactions id and items
id = []
items = []
for i in range(0, len(transactions)):
    for j in transactions[i]:
        id.append(i)
        items.append(j)

datatransed = pd.DataFrame(id, columns=['id'])    
datatransed = pd.concat([datatransed, pd.DataFrame(items, columns=['items'])], axis=1)
print(datatransed.head)


#%%
def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1

# make one hot key for items
hot_encoded_df=datatransed.groupby(['id','items'])['items'].count().unstack().reset_index().fillna(0).set_index('id')
hot_encoded_df = hot_encoded_df.applymap(encode_units)

frequent_itemsets = apriori(hot_encoded_df, min_support=0.02, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=0.5)

print("频繁项集：", frequent_itemsets)
print("关联规则：", rules[ (rules['lift'] >= 1) & (rules['confidence'] >= 0.3) ])



