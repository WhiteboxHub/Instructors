import numpy as np

from numpy import random
myrandom = random.randint(90,100)
print(myrandom)

my_rand_float = random.rand(1,10)
print(my_rand_float)

print(my_rand_float.shape)
my_rand_float[0,1]=22
print(my_rand_float)
#declaring random int with sepsified size of the array

x = random.randint(5,55,size=(3,5))
print(x)


#Data Distributioin

y = random.choice([1,2,4,5,6],p=[0.3,0.15,0.32,0.05,0.18],size=(100))
print(y)

#shuffle the array

arr = np.array([1,2,3,4,5,6,7])
myshuffle = random.shuffle(arr)
print(random.permutation(arr))