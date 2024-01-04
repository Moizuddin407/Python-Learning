import numpy as np
# Q1
arr = np.array([1,2,3,4,5,6,7,8,9])
# Q2
matrix = np.random.rand(3,3)

# Q3
arr = arr.reshape(3,3)
add_Matrix = arr + matrix
subtract_Matrix = arr - matrix
mult_Matrix = arr * matrix
div_Matrix = arr / matrix

# Q4
mean = np.mean(arr)
median = np.median(arr)
std_dev = np.std(arr)

# Q5
arr = arr.reshape(9)
# Q6
greater_than_5 = arr[(arr>5)&(arr<9)]

# Q7
arr = arr.reshape(3,3)

# Q8
hstack_arr = np.hstack([arr,matrix])

vstack_arr = np.vstack([arr,matrix])

# Q9
result = np.multiply(matrix, arr)

# Q10
# Can also give command like:max_value = np.amax(arr[1,:])
# [1,3:] means columns from 3 till end and arr[1,:3] means
# columns from 0 till 2

max_value = np.amax(arr)
max_index = np.argmax(arr)

min_value = np.amin(arr)
min_index = np.argmin(arr)

# Q11
summed_arr = arr*matrix

# Q12
matrix2 = np.array([[10,11,12],[13,14,15],[16,17,18]])
variance = np.var(matrix2)
