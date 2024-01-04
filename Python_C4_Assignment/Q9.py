'''
Given two NumPy arrays:
import numpy as np
arr1 = np.array([1, 2, 3, 4]) arr2 = np.array([5, 6, 7, 8])
Find the common elements between the two arrays
'''

arr1 = np.array([1, 2, 3, 4]) 
arr2 = np.array([4, 6, 7, 8])

arr3=np.intersect1d(arr1,arr2)
print(arr3)