import numpy as np
import sys
myArr = np.array([[3, 6, 8, 9], [7, 9, 1, 5]], np.int8)
print(myArr[1, 3])
listArray  = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(listArray)
print(listArray.dtype)
print(listArray.shape) #returns the dimensions of array
print(np.zeros((2, 5))) #makes a new 2d array
rng = np.arange(6, 6)
print(rng)
lSpace = np.linspace(1, 10, 5) # this code is actually producing elements between 1 to 5 in 12 entries
print(lSpace)
emp = np.empty((7,2)) # creates an empty array of 1R 2C with random values
print(emp)
empLike = np.empty_like(lSpace) # copies the size of an existing array and creates a new array
print(empLike)
ide = np.identity(5) # creates a 5x5 identity matrix
print(ide)
arr = np.arange(100)
print(arr.reshape(2, 50)) # reshapes a matrix into a valid RxC
print(arr.ravel())
newArr = np.array([[1, 2, 3], 
                    [4, 5, 6], 
                    [7, 8, 9]])
print(newArr.sum(axis=1), newArr.sum(axis=0))
# 2d array has 2 Axis (axis=0 X and axis = 1 Y) the axis are use to perform operations depending on rows and columns
print(newArr.T) # to transpose a matrix
newArr.flat # gives an iterator for printing all the values
# for item in newArr.flat:
#     print(item)
print(newArr.ndim) # returns no. of dimensions
print(newArr.size)
print(newArr.nbytes) # returns no. of bytes used 
# these functions can also take axis as an argument
print(newArr.argmax()) # returns max value index in array
print(newArr.argmin()) # returns min value index of array
print(newArr.argsort()) # will sort the array
#print(newArr.reshape(1, 3)) # reshapes the dimension of array
print(newArr+newArr) # applies arithematic operations(+, -, *, /) on two arrays. 
print(np.sqrt(newArr)) # square root of all elements
print(newArr.max(), newArr.min()) # max/min value in array
print(np.where(newArr==7)) # returns the indexes where a conditions becomes true
print(np.count_nonzero(newArr)) # counts non zero elements
print(np.nonzero(newArr)) # returns indexes of all the in a an array non zero elements
py_ar = [9, 1, 3, 5]
np_ar = np.array(py_ar)
print(sys.getsizeof(1)*len(py_ar))
print(np_ar.itemsize * np_ar.size)
