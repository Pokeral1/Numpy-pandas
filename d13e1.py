import pandas as pd
df=pd.read_csv('employees.csv')
print(df.head())#prints first 5 rows
print(df.tail())#prints last 5 rows
print((df.describe()).round(0))#gives mean, std, min, count, .25, .50, .75, max
#The average salary is 66900, and youngest person is aged 24 years
print(df.info())
print(df.shape)