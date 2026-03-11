import numpy as np
arr=np.array([np.random.randn(1000)])
count = np.sum((arr > -1) & (arr < 1))
print("No of numbers between -1 and 1 : ", count)
print("Normal Distribution : ",np.where(np.isclose(count/1000,.68,.05),'Yes','No'),' ',count/1000)

