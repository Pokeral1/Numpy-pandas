import numpy as np

np.random.seed(42)

students = ['Alice', 'Bob', 'Carol', 'Dave', 'Eve',
            'Frank', 'Grace', 'Hana', 'Ian', 'Jay']

# 10 students, 5 subjects: Math, Science, English, History, Computer
marks = np.random.randint(40, 101, (10, 5))

subjects = ['Math', 'Science', 'English', 'History', 'Computer']
def task1 (marks):

    print("Marks of students : ", marks)
    print("Shape of array : ",marks.shape)
    print("Average of students",np.mean(marks))

def task2(marks):
    print("Average per student : ",np.mean(marks,1))
    print("Highest marks of student : ",np.max(marks,1))
    print("Result : ", np.where(np.mean(marks,1)>=80,'Distinction',(np.where(np.mean(marks,1)>=50,'Pass','Fail'))))
def task3 (marks,subjects):
    averagePerSubject=np.mean(marks,0)
    print("Average per subject : ",averagePerSubject)
    print("Average per subject sorted : ",averagePerSubject)
    print("Highest marks in : ",subjects[np.argmax(averagePerSubject)])
    print("Lowest marks in : ",subjects[np.argmin(averagePerSubject)])
def task4(marks, students):
    students=np.array(students)
    avg = np.mean(marks, axis=1)
    topper_index = np.argmax(avg)
    print("Topper:", students[topper_index],
          "has an average of", avg[topper_index])
    print("Names of students with marks in serial (descending) order:\n",
          students[np.argsort(avg)[::-1]],'\nMarks', (avg)[::-1])
def task5(marks,students,subjects):
    students=np.array(students)
    print("Names of students who failed : ",students[np.where(np.mean(marks,1)<50)])
    print("Names of students who above 90 in any subject: ",students[np.where(np.max(marks,axis=1)>90)])
    print("All Marks of students who scored highest in computer : ",marks[np.argmax(marks[:,subjects.index('Computer')])])
task1(marks)
task2(marks)
task3(marks,subjects)
task4(marks,students=students)
task5(marks,students,subjects)
