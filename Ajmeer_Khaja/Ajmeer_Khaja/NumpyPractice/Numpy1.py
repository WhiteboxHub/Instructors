import numpy as np

arr = np.array([1,2,3,4,5])
print(arr)
print(np.__version__)
print(type(arr))


myint = np.array(30)
print(myint)
print(type(myint))
print(myint.ndim)
print(arr.ndim)

my5darr = np.array([1,2,4,3,2],ndmin=4)
print(my5darr.ndim)
print(my5darr.dtype)


animals = np.array(['dog',
                    'cat',
                    'horse'
                    ,'hen'
                    ,'cow'
                    ,'bull'
                    ,'donkey'])
print(animals)

strnums = np.array([1,2,4,3,2],dtype='S')
print(strnums.dtype)
print(animals.dtype)
print(strnums)

#convering the data type of nparray

stringnums = arr.astype('U')
print(stringnums.dtype)
print(stringnums)

#copying an np array and changing the values


newarray = np.array([1,3,4,2,4,2,10])
copyarray = newarray.copy()

copyarray[0]=20
copyarray[2]=22
print(newarray,copyarray)



x = newarray.view()
newarray[0]=99
print(newarray)
print(x)
print(copyarray.base)
print(x.base)
print(x.shape)