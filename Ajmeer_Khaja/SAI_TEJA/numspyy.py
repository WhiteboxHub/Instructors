import numpy as np


#0 dimentional array
arr0 = np.array([42]) 
print(arr0)

# 1 Dimentional array
arr1 = np.array([1,2,3,4,5,6,7]) 
print(arr1)

# 2 dimentional array
arr2 = np.array([[1,2,3,4,5],[6,7,8,9,10]]) 
print(arr2)

# 3 dimentional array with 2d array
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr3) 


#chek the how many dimensions

print(arr0.ndim)
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)

# higher dimensional array

arr = np.array([1, 2, 3, 4], ndmin=6)

print(arr)
print('number of dimensions :', arr.ndim)



# access indexing elements.....                      
print('access element:-',arr1[0]) # for 1D
print('access the 2D element:-',arr2[0,1]) # for 2D
print('negative index',arr2[1,-1])
print('access the 3D:-', arr3[0,1,2])



# 1D slicing elements......
print('1d array slicing:-',arr1[1:5])
print('1d array slicing:-',arr1[1:])
print('1d array slicing:-',arr1[:6])
print('1d array slicing:-',arr1[-3:-1])

# 1D step...
print(arr1[1:5:2])
print(arr1[::2])

#2D slicing
print(arr2[1,1:4])
print(arr2[0:2,2]) # if the both are return index 2(selection)
print(arr2[0:2,1:4]) # 1st one is row indexing 2nd is coloum indexing




