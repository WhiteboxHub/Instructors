import numpy as np
import os
print(os.getcwd())
a = np.array([1,2,3,4,5])
print(a)
b = np.array([11,22,33,44,55])
print(b)
varr = np.vstack((a,b))
print(varr)
# with open('data.txt','r') as file:
datafile = 'data.txt'

data = np.genfromtxt(datafile,delimiter=',')
print(data)
print('the size of data.txt is :',data.shape)
##advance indexing and boolean masking
mod = np.where(data%3 ==0)
print('the module of 2 is',mod)

print(data > 50)

print(data[data>39])

##split the array into specifid pats

split = np.array_split(data,5)
print(split)

print('the num is ata' ,np.where(data ==9.00))