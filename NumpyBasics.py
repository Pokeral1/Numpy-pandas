import numpy as np
scores=np.array([85, 90, 78, 92, 88])
double=scores*2 #no loop needed, vectorization allows us to perform operations on the entire array at once
print("Original scores:", scores) 
print("Doubled scores:", double)
a = np.array([1, 2, 3, 4, 5])

# Arrays of zeros and ones — useful for placeholders
listOfZeros=np.zeros(5)          # [0. 0. 0. 0. 0.]
Matrix=np.zeros((3, 3))     # 3x3 grid of ones

# Like range() but for NumPy
even=np.arange(0, 10,2)  # [0 2 4 6 8]  syntax---(start, stop, step)

# 5 evenly spaced values between 0 and 1
values=np.linspace(0, 1, 5) # [0.   0.25  0.5  0.75  1.0] syntax---(start, stop, noOfValues)
print("Array of zeros:", listOfZeros)
print("Matrix of ones:", Matrix)
print("Even numbers:", even)
print("Linspace values:", values)

a=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24])
b=a.reshape(2,12) # Reshape the 1D array into a 2D array with 2 rows and 12 columns
print("Original array:", a)
print("Reshaped array:\n", b)