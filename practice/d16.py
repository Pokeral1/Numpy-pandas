import pandas as pd
df=pd.read_csv('employees.csv')
def ex1(df):
    df['annual salary']=df['salary']*12
    df['tax']=df['annual salary']*0.2
    df['net salary']=df['annual salary']-df['tax']
    return df
def ex2(df):
    def level(experience):
        if experience>=10:
            return 'Senior'
        elif experience>=5:
            return 'Mid'
        else:
            return 'Junior'
    df['level']=df['experience'].apply(level)
    df['salary_band'] = df['salary'].apply(
    lambda x: 'High' if x > 70000 else ('Mid' if x > 50000 else 'Low'))
    return df
def ex3 (df):
    df['dept_code']=df['department'].map({
        'HR': 1,
        'IT': 2,
        'Finance': 3
    })
    df['name_upper']=df['name'].str.upper()
    df['name_length']=df['name'].str.len()
    return df
df=ex1(df)
df=ex2(df)
df=ex3(df)
print(df[['name_upper','name_length','level','salary_band','dept_code']])