'''
Given a 2D NumPy array:
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
Calculate the sum of all the elements in the array.
'''

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
n=len(arr)
m=len(arr[0])
sum=0
for i in range(n):
    
    for j in range(m):
        sum+=arr[i][j]

print(sum)