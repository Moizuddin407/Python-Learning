# Quick notes
import numpy as np

## Create arr:
arr = np.array([1,2,3])
arr = np.full((2,2),1,dtype='int')

## Check arr info:
# For array dimension
arr.ndim 
# For array Shape:
arr.shape
# For reshaping:
arr.reshape(size)

## Accessing in arr:

# get specific row,col value 
arr[1,5]

# get specific row:
arr[0,:]
# get specific col:
arr[:,0]

# get specific row(s) and col(s) with step size:
arr[0:2:1,0:2:1]

## Initializing arr:

# any number
arr3 = np.full((2, 2), 1, dtype="int32")

# full_like(to use shape of a previously built arr)
# (arr_to_shape_like,number,datatype)
np.full_like(arr3,4,dtype="int32")

# rand numbers (row,col)
np.random.rand(4,2)

# rand numbers according to previously built shape:
np.random.random_sample(arr3.shape)

# random int generation(start,end,nxn arr)
np.random.randint(1,7,size=(3,3))

## Maths:
# identity matrix
np.identity(5)
# repeat an array
arr = np.array([1,2,3])
r1=np.repeat(arr,3,axis=0)
print(r1)

# to avoid changing value of a when changing b, use copy
a=np.array([1,2,3])
b=a.copy()
b[1]=0
print(a)
print(b)

# Basic maths in numpy:
a = np.array([1,2,3,4])
b= np.array([1,2,3,4])
# a+=2 also correct
print(a+2)
print(a-2)
print(a/2)
print(a*2)
print(a+b)

print(a*a*a)

# trigonmetry:
np.sin(a)
np.cos(a)
np.tan(a)

# LA
a= np.full((2,3),1)
b=np.full((3,2),2)
print(a)
print(b)

# somewhat similar to np.dot
np.matmul(a,b)
# Create identity matrix
c = np.identity(3)
# determinant
np.linalg.det(c)


## Operations to be performed on arrays:
arr+arr
# All others like -,/,* can be performed similarly

##Stats
arr=np.array([[1,2,3],[4,5,6]])
# for overall
np.min(arr)
# for each:
np.min(arr,axis=1)
np.max(arr)

# check for row and col
np.sum(arr)


# Dot product:
np.dot(arr,arr2)

## Reorganizing:

# reorganizing/reshaping arr:
before = np.array([[1,2,3],[4,5,6]])
after = before.reshape(2,3)
print(after)

# Vertical stack:
np.vstack([before,after,before])

# Horizontal stack

np.hstack([before,after])

## Loading data from file:
filedata = np.genfromtxt('C:\\Users\\MOIZ UDDIN\\Desktop\\SampleFileLoad.txt', delimiter=",")

# Remove NaN values
cleaned_data = filedata[~np.isnan(filedata)]

cleaned_data.astype('int32')
print(cleaned_data)

# Advanced Indexing:
# Shows where in arr values are > 50
cleaned_data > 50
# SHows val > 50
arr = cleaned_data[cleaned_data > 50]
print(arr)
# Specific indexes
aer=arr[[2,3,9]]
print("\n",aer)

# Checking which columns have values > 50
np.any(cleaned_data > 50, axis = 0)

np.all(cleaned_data > 50, axis = 0)
# ~ means not

## Extra func:
# get type
a.dtype
# getsize
a.itemsize
# get totalsize (a.itemsize * a.size) 
a.nbytes
b.nbytes