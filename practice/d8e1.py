import numpy as np
scores = np.array([45, 82, 67, 91, 55, 78, 88, 43, 76, 95])
names =  ['Ana','Ben','Cal','Dev','Eve','Fay','Gil','Hana','Ian','Jay']
print(scores[scores>70])
print(scores[(scores<50) | (scores>90)])
result=np.where(scores>=85,'Distinction',np.where(scores>=50,'Pass','Fail'))
print(result)
order=np.argsort(scores)[::-1]
print(scores[order])
sorted_names = np.array(names)[np.argsort(scores)]
print(sorted_names[::-1])