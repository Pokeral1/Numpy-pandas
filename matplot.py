import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
plt.plot([1, 2, 3], [10, 20, 15])
plt.show()


months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales  = [15000, 18000, 14000, 22000, 19000]
plt.plot(months, sales)
plt.show()


departments = ['HR', 'IT', 'Finance']
avg_salary  = [44667, 66000, 90333]
plt.bar(departments, avg_salary)
plt.show()


age    = [25, 30, 35, 28, 42, 38]
salary = [45000, 62000, 71000, 50000, 85000, 91000]
plt.scatter(age, salary)
plt.show()


salaries = [45000, 62000, 47000, 65000, 85000, 58000, 91000, 69000, 41000, 95000]
plt.hist(salaries, bins=100)
plt.show()


plt.plot(months, sales)
plt.title('Monthly Sales 2024')
plt.xlabel('Month')
plt.ylabel('Sales (₹)')
plt.show()


plt.plot(months, sales, color='steelblue', linewidth=2, marker='o')
#                                                         ^^^^^^^^
#                                          adds a dot at each data point
plt.bar(departments, avg_salary, color=['#FF6B6B', '#4ECDC4', '#45B7D1'])
# pass a list of colors for different bars

