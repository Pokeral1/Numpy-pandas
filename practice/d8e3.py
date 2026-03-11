import numpy as np
students = np.array([[88, 72, 91],
                     [45, 60, 55],
                     [78, 85, 90],
                     [50, 48, 62]])
avgperStud=np.mean(students,1)
goodStud=avgperStud>70
print(students[goodStud])
