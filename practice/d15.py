import pandas as pd
df=pd.read_csv('employees_messy.csv')
def ex1(df):
    print(df.isnull().sum())
    print(df.isnull().sum().sum())
    return df
def ex2(df):
    print(df.shape)
    df=df.drop_duplicates()
    print(df.shape)
    df['age']=df['age'].fillna(round(df['age'].mean(),0))
    df['salary']=df['salary'].fillna(df['salary'].median())
    df['experience']= df['experience'].fillna(0)
    print(df.isnull().sum())
    return df
def ex3(df):
    df.rename(columns={'name':'full_name','experience':'exp_years'},inplace=True)
    df['salary'] = df['salary'].astype(float)
    print(df.dtypes)
    print(df)
    
    
df=ex1(df)
df=ex2(df)
ex3(df)