import numpy as np
studentsMarks=np.array([np.random.randint(40,101,20)])
studentMarks=np.reshape(studentsMarks,(5,4))#reshape the array to 5 rows and 4 columns
''' The above way is same as below
studentMarks=np.array([np.random.randint(1,101,20)]).reshape(5,4)
                    or      
studentMarks=studentsMarks.reshape(5,4)'''
print(studentMarks)
print("Average of each student ", np.mean(studentMarks,1))
print("Highest score of each student ",np.max(studentMarks,1))
print("Result = ",np.where(np.mean(studentMarks,1)>=60,'Pass','Fail'))