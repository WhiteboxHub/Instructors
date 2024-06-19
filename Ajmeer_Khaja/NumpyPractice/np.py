import numpy as np


x = np.array([2,3,4,5,6])
print(x)

def sortnparray(arr):
	print(f"Given Array is {arr}")
	sortedarr = np.sort(arr)
	print(f"Sorted Array is {sortedarr}")


sortnparray([12,34,52,45,2,4,5232,523,52,89])
