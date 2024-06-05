import numpy as np
'''a=np.array([10])
print(a)
a=np.array([10,12,14])
print(a)
a=np.array([[10,12,14],[16,15,13]]) #2D array
print(a)
a=np.array([[[11,22,33],[44,55,66],[77,88,99],[00,11,22]]])  #3D array
print(a)


a=[10,20,30]
b=np.asarray(a,dtype=float) #here we have two inputs 
print(b)
'''
a=[[10,20],[11,22]]
b=np.asarray(a,order="C") # c-row major order
#print(b)
for i in np.nditer(b):
    print("row major order:",i)
    
b=np.asarray(a,order="F") #colum major order
for i in np.nditer(b):
  print("colum major order:",i)
  

#frombufferarray
a=b"welcome to NumPy in python"
c=np.frombuffer(a,dtype="S1",count=12,offset=5)
print(c)


#from fromiter()
a=[10,20,30,40]
b=np.fromiter(a,dtype=int,count=4)
print(b)

a=np.full([2,3],1)
print(a)

a=np.full([2,3,4],10)
print(a)


#----------------------------------------------->
#how to check dimesnsions arry 
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


#create an array with 5 dimensions and verify that 
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim)




