import pandas as pd
import numpy as np

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
check_nan = df2['Min.Price'].isnull().values.sum()
check_nan2 = df2['Max.Price'].isnull().values.sum()

# df2['Min.Price'] = df2['Min.Price'].fillna(0)
# df2['Max.Price'] = df2['Max.Price'].fillna(0)  # or should I use replace??
# print(df2.where(df2['Min.Price'] == 0.0))

min_price_mean = df2.iloc[:].mean()["Min.Price"]
max_price_mean = df2.iloc[:].mean()["Max.Price"]

df2['Min.Price'] = df2['Min.Price'].fillna(min_price_mean)
df2['Max.Price'] = df2['Max.Price'].fillna(max_price_mean)

print('\n\n' + 'now replace 0s with the mean across rows?')
# df2.loc[df2, ['Min.Price', 'Max.Price']] = df2.mean(axis=1) --> attempt 1
# df2['Min.Price', 'Max.Price'].iloc[:].mean(axis=1) --> attempt 2
# df2.loc[df2[df2['Min.Price', 'Max.Price'].isnull()]] = df2.mean(axis=1) --> what am I even doing T-T
# df2.loc[df2.where(pd.Series(range(98))), ['Min.Price', 'Max.Price']] = df2.mean(axis=1) --> help......

# try to only filter the rows with 0 values and replace those with the respective mean?
# or is it the mean of each column instead of 0s that replace nulls
# print(df2)

# bruh there aren't any null values anymore
print(f'# of NaN in Min.Price column: {check_nan}')  # 7
print(f'# of NaN in Max.Price column: {check_nan2}')  # 5


# print('\n\n')
# print(df.columns)

'''
3) How to get the rows of a dataframe with row sum > 100?
df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
'''

# what does row sum even mean -_-
# why would I sum up all the rows???
print(df.columns)
print(df.dtypes)

'''
4)Create a 4x4 NumPy array filled with random integers between 1 and 100. 
Then, reshape this array into two separate 2D arrays, where one represents the rows and the other 
represents the columns. Write a function, preferably using a lambda function, to calculate the sum 
of each row and each column separately, and return the results as two separate NumPy arrays
'''

# lambda is a function that is just faster syntax as a normal function
# lambda to calculate the sum of each row and column separately, return 2 separate NumPy arrays

sum = lambda a, b: a + b
print(sum(5, 5))
total_sum = list(filter(lambda nums: ...)) # some sum for row, do the same for columns --> 2x2
# or then I can 1) create the array 2) lambda 3) sum of each
# https://www.w3resource.com/python-exercises/lambda/python-lambda-exercise-23.php
