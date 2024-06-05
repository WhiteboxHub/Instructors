import numpy as np

'''a=np.zeros(3)
print(a) #1D array
#2D array
a=np.zeros([2,3])
print(a)
a=np.zeros([2,3,3])
print(a)
#--------------------------------------------------->

#full()
a=np.full([2,3],1) #it will be print all 1
print(a)
 
a=np.full([2,3,4],10) #it will print all 10
print(a)

#random.rand()
a=np.random.rand(2,4) #evertym it changes while prints the code
print(a)  

#ones -it will be print float values
a=np.ones([2,3])
print(a)

#eyes-it print diag elemnts with float values
a=np.eye(5)
print(a)

#range
a=np.arange(10,20,1)
print(a)

a=np.arange(10,100,10,dtype=float)
print(a)



#-------------------------------------------------------------->
#indexing
arr=np.array([1,2,3,4])
print(arr[1])

#add array element
arr=np.array([1,2,3,4])
print("adding two indexing elements:",arr[2]+arr[3])

arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])#2-arrays
print("2nd element on 1st row:",arr[0,1])
print(arr.ndim)

arr=np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]) #3D-array
print(arr[0,1,2])
print("type of array is:",arr.ndim)

#------------------------------------------------------------------->
#slicing
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5]) #slicing elements from 1to 5
print(arr[1:5:2]) 
print(arr[:4])
print(arr[1:])
print(arr[::2])


arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr.ndim)
print(arr[1, 1:4])
print(arr[0:2, 1:4])
'''

#-------------------------------------------------------------->
#datatypes in NumPy in python
arr = np.array([1, 2, 3, 4])
print(arr.dtype) 

arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)


arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)

#---------------------------------------------------------------->
#Print the shape of a 2-D array:
arr = np.array([[1, 2, 3], [5, 6, 7]])
print(arr.shape)

#creating an array with 5 dimensions
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('shape of array :', arr.shape)
print(arr.ndim)
