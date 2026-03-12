import pandas as pd
s = pd.Series([85, 92, 78], index=['Alice', 'Bob', 'Carol'])
print(s[85])  # This will raise a KeyError because 85 is not an index label
print(s['Alice'])  # This will print 85, as 'Alice' is the index label for that value
data = {
    'name':   ['Alice', 'Bob', 'Carol', 'Dave'],
    'age':    [25, 30, 27, 35],
    'salary': [50000, 62000, 47000, 71000]
}

df = pd.DataFrame(data)
print(df)