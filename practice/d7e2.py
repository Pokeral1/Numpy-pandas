import numpy as np
marks = np.array([[72, 88, 91, 65],
                  [80, 76, 85, 90],
                  [60, 95, 78, 82]])
avgPerSub=np.mean(marks,axis=0)
avgPerStud=np.mean(marks,axis=1)
print(avgPerStud)
print(avgPerSub)
print("Highest marks = ",np.max(marks))
print(np.argmax(avgPerSub))