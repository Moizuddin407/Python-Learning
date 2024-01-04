# Guideline:https://www.youtube.com/watch?v=QUT1VHiLmmI

# numpy self learned
# numpy faster as it uses fixed types
import numpy as np
a = np.array([1,2,3])
# print(a)

# can specify which type of data to store:
a = np.array([1,2,3], dtype='int32')
b = np.array([[9.0,8.7,4.6],[2.4,5.4,9.8]])
# print(b)
# getting dimensions for array
a.ndim
# getting shape of arr
b.shape
# get type
a.dtype
# getsize
a.itemsize
# get totalsize (a.itemsize * a.size) 
a.nbytes
b.nbytes




# Accessing specific elements
newarr= np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
newarr.ndim
newarr.shape
newarr.dtype
# getting specific element [r,c]
newarr[1,5]
# Same can be done by -ve index
# i.e. newarr[1,-2] (second row second last col)

# get a specific row (row num, : for slicing whole row):
newarr[0,:] 

# get a specific col (for slicing whole col : , row num ):
newarr[:,2] 

# get a specific col (for slicing whole col : , row num ):
newarr[:,2]

# specific rows and col [startindex:endindex:stepsize]
newarr[0, 1:6:1]

# Access rows 0 to 1 and columns 4 to 6
subset = newarr[0:2, 3:6]
print(subset)

# changing vals:
newarr[1,5] = 20
newarr[:,2] = 5




# checking 3d functions
b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)

b[0,1,1]

 
 # initializing different arrs
# any number
arr3 = np.full((2, 2), 1, dtype="int32")
# print(arr3)
# full_like(to use shape of a previously built arr)

np.full_like(arr3,4,dtype="int32")

# rand numbers
np.random.rand(4,2)

# rand numbers according to previously built shape:
np.random.random_sample(arr3.shape)

# random int generation(start,end,nxn arr)
np.random.randint(1,7,size=(3,3))



# identity matrix
np.identity(5)
# repeat an array
arr = np.array([1,2,3])
r1=np.repeat(arr,3,axis=0)
print(r1)



# quiz
arr = np.full((5,5),1)
arr[1:4,1:4]=0
arr[2,2]=9
print(arr)

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

np.matmul(a,b)
# np.dot



c = np.identity(3)
# determinant
np.linalg.det(c)



#Stats
arr=np.array([[1,2,3],[4,5,6]])
# for overall
np.min(arr)
# for each:
np.min(arr,axis=1)
np.max(arr)

# check for row and col
np.sum(arr)




# reorganizing/reshaping arr:
before = np.array([[1,2,3],[4,5,6]])
after = before.reshape(2,3)
print(after)

# Vertical stack:
np.vstack([before,after,before])

# Horizontal stack

np.hstack([before,after])



# Loading data from file:
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