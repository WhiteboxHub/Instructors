import numpy as np
from numpy import random

fnp = np.full((4,4),9,dtype=int)
print(fnp)

rnp = fnp.reshape((2,8))
print(rnp)

#practing the flatten array

arr = np.array([1,2,3,4,2,9])
arr1 = np.array([9,2,3,4,2,8])

flatarr = np.array([arr,arr1]).flatten("F")
print(flatarr)


rarr = np.random.randint(4,44,size=(6,6))
print(rarr)


print(np.transpose(rarr))


print(np.add(arr,arr1))
print(np.subtract(arr,arr1))
print(np.multiply(arr,arr1))
print('flat array')
print(np.dot(flatarr,flatarr))

print(arr)
print(np.sqrt(arr))
print(np.log(arr))


print(np.linalg.inv(rarr))