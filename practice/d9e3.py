import numpy as np
np.random.seed(99)
sales = np.random.randint(500, 5000, 10)
products = ['A','B','C','D','E','F','G','H','I','J']
prices=np.argsort(sales)[::-1]
print(sales[prices])
for i in range (sales.size):
    print("Product ",products[prices[i]],": ",sales[prices[i]])
