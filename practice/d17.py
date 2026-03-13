import pandas as pd

df = pd.read_csv('employees.csv')

def ex1(df):
    r1 = df.groupby('department')['salary'].agg(
        avg_salary='mean',
        max_salary='max',
        min_salary='min',
        head_count='count'
    )

    print(r1)

    averageExperience = df.groupby('department')['experience'].mean()
    print(averageExperience.sort_values(ascending=False))

    return r1


def ex2(df):

    def level(experience):
        if experience >= 10:
            return 'Senior'
        elif experience >= 5:
            return 'Mid'
        else:
            return 'Junior'

    df['level'] = df['experience'].apply(level)

    r1 = df.groupby(['department','level'])['salary'].mean().reset_index()

    print(r1)


def ex3(df):
    # Pivot table 1 — avg salary by dept and level
    p1 = df.pivot_table(values='salary', index='department',
                        columns='level', aggfunc='mean')
    print(p1)

    # Pivot table 2 — avg salary AND experience by dept
    p2 = df.pivot_table(values=['salary','experience'],
                        index='department', aggfunc='mean')
    print(p2)


r1 = ex1(df)
ex2(df)
ex3(df)

#print(df)