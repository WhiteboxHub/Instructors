import numpy as np

#Iterating arrays

print("1D array:-")
arr = np.array([1, 2, 3])
for x in arr:
  print(x)

print("2D arrays:-")

arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  print(x)


print("each scaler element of the 2D array:-")

arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  for y in x:
    print(y)


print("iterating 3D arrays:-")

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
  print("x represents the 2-D array:")
  print(x)


print("iterate the arrays in each dimension:--")

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
  for y in x:
    for z in y:
      print(z)


#Array using nditer()
      
print("iterating on eaach scaler element:-")

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
  print(x)

#iterating with different step size
  
print("Iterate through every scalar element of the 2D array skipping 1 element:-")

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr[:, ::2]):
  print(x)




#Enumerated iteration using ndenumerate()

print("Enumerate on following 1D arrays elements:-")

arr = np.array([1, 2, 3])
for idx, x in np.ndenumerate(arr):
  print(idx, x)

print("Enumerate on following 2D arrays elements:-")

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(arr):
  print(idx, x)



#Numpy joining array
print("joining NnmPy arrays")
print("join two arrays:-")

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)

#along rows (axis=1)
print("Join two 2-D arrays along rows (axis=1):-")

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)


#stack functions...

print("Joining Arrays Using Stack Functions:-")

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)
print(arr)


#splitting numpy arrays...
print("split the array in 3 parts:-")

arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)

print("split the array in 4 parts:-")

arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 4)
print(newarr)

print("access the splitted arrays:-")

arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr[0])
print(newarr[1])
print(newarr[2])
print(newarr)

print("split the 2D arrays into three 2D arrays:-")

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr)

#using hsplit()
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.hsplit(arr, 3)
print(newarr)





