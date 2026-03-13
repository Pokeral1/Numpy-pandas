import matplotlib.pyplot as plt
import pandas as pd 
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales  = [15000, 18000, 14000, 22000, 19000]
departments = ['HR', 'IT', 'Finance']
avg_salary  = [44667, 66000, 90333]
plt.plot(months, sales, color='steelblue', linewidth=2, marker='o')
#                                                         ^^^^^^^^
#                                          adds a dot at each data point
plt.show()
plt.bar(departments, avg_salary, color=['#FF6B6B', '#4ECDC4', '#45B7D1'])
plt.show()