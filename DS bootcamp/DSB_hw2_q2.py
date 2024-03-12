
# coding: utf-8

# In[5]:


'''
2) Replace missing values in Min.Price and Max.Price columns with their respective mean (check documentation).
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
'''
import pandas as pd
import numpy as np


# In[17]:


'''
1) From df filter the 'Manufacturer', 'Model' and 'Type' for every 20th row starting from 1st (row 0).
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
'''
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
# df.columns --> there's 27 rows
# print(df.filter(items=['Manufacturer', 'Model', 'Type'])) --> all rows
print(df.loc[::20, ['Manufacturer', 'Model', 'Type']])

'''
2) Replace missing values in Min.Price and Max.Price columns with their respective mean (check documentation).
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
'''
print('\n\n')
print(df.filter(items=['Min.Price', 'Max.Price']))
# look for null values, NaN (not a number)

# if I understand this right, replace NaN with the mean of each row???
# or column??
# -_-

df2 = pd.DataFrame(df, columns=['Min.Price', 'Max.Price'])
df2


# In[18]:


df2


# In[10]:


check_nan = df2['Min.Price'].isnull().values.sum()
check_nan2 = df2['Max.Price'].isnull().values.sum()

check_nan, check_nan2


# In[23]:


min_price_mean = df2.iloc[:].mean()["Min.Price"]
max_price_mean = df2.iloc[:].mean()["Max.Price"]

min_price_mean, max_price_mean


# In[24]:


df2['Min.Price'] = df2['Min.Price'].fillna(min_price_mean)
df2['Max.Price'] = df2['Max.Price'].fillna(max_price_mean)
df2

