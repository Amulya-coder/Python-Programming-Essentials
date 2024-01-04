'''
Given a 2D NumPy array:
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
Calculate the sum of each row and each column separately
'''

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

n=len(arr) # length of rows
m=len(arr[0]) # column length

# sum of each row
for i in range(n):
    sum=0
    for j in range(m):
        sum+=arr[i][j]
    print(f'Sum:{i},{sum}')

# sum of each column
for i in range(m):
    sum=0
    for j in range(n):
        sum+=arr[j][i]
    print(f'Sum:{i},{sum}')