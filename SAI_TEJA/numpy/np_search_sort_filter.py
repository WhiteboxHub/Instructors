import numpy as np
#search
print("find the indexes where the value is 4:-")

arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)

print("find the indexes where the values are even:-")

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0)
print(x)

#search sorted...
print("Find the indexes where the value 7 should be inserted:-")

arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
print(x)

print("Find the indexes where the value 7 should be inserted, starting from the right:-")

arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7, side='right')
print(x)



#sorting arrays

print("sort the array:-")

arr = np.array([3, 2, 0, 1])
print(np.sort(arr))

#aphabetically
 
print("sort the array alphabetically:-")

arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr))

# boolean

print("sort a boolean array:-")

arr = np.array([True, False, True])
print(np.sort(arr))

#sorting a 2D array

print("sort a 2D array:-")

arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))

# filter..

arr = np.array([41, 42, 43, 44])
x = arr[[True, False, True, False]]
print(x)


print("Create a filter array that will return only values higher than 42:-")
arr = np.array([41, 42, 43, 44])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)