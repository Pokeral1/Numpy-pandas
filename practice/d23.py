import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("sales.csv")
plt.plot(df['month'], df['revenue'])

monthly = df.groupby('month')['revenue'].sum()

plt.plot(monthly.index, monthly.values, color='steelblue', marker='o')

plt.show()