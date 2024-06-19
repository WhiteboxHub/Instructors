import numpy as np
import math
from numpy import random
#print an array  

arr = np.array([1,5,4,5,2,3,5,2])
print(arr)

##creating a array with zero value in dimention of 3,5
npz = np.zeros((5,5))
print(npz)

##changeing the center values of the array

for i in range(1,4):
    for j in range(1,4):
        npz[i,j] = 1
print(npz)

##Changing the center value of th enp array
npz[2,2]= 9
print(npz)

#create an aray with x,y dimension with zeros and also with ones

znp = np.zeros((5,8))
print(znp)

onp = np.ones((5,5))
print(onp)

for i in range(0,len(znp)):
    for j in range(0,len(znp[0])):
        if i%2 !=0 and j%2 !=0:
            znp[i,j]=9
print(znp)


eyenp = np.eye(10)
print(eyenp)

for i in range(len(eyenp)):
    for j in range(len(eyenp[0])):
        if i!=j:
            eyenp[i,j] = 3
print(eyenp)

for i in range(len(eyenp)):
    for j in range(len(eyenp[0])):
        if len(eyenp)-j-1 == i:
            eyenp[i,j] = 9

print(eyenp)


arangenp = np.arange(0,199,33)
print(arangenp)
lspace = np.linspace(1,55,20)
##convering the decemials to its ceil value

for i in range(len(lspace)):
    lspace[i]= math.ceil(lspace[i])
print(lspace)
# reshp = arangenp.reshape(len)
# print(reshp)

rint  = np.random.randint(0,20,size=(5,5))
print(rint)