import numpy as np
arr=np.random.randint(1,101,10)

print(np.mean(arr))
c=np.sum(arr>np.mean(arr))
print(c)
