import pandas as pd
df=pd.read_csv('employees.csv')
def ex1(df):
    print(df[['name','salary']])
    print(df[df['department']=='IT']['name'])
    print(df[(df['salary']>60000) & (df['age']<35)])
def ex2(df):
    print("Excerside 2")
    print(df.loc[0:3, ['name','salary']])
    print(df.iloc[-3:, :2])
    print(df.loc[df['department']=='Finance'])
def ex3(df):
    print(df['department'].value_counts())
    print(df[(df['experience']>5)].sort_values('salary',ascending=False))
ex1(df)
ex2(df)
ex3(df)