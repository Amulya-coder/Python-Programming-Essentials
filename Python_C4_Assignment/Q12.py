# Create a NumPy array with 20 random integers between 1 and 100 (inclusive). Find the
# maximum value and its index in the array.

arr=np.random.randint(1,101,(1,20))
print(arr.max()) # Finding the max value
print(np.argmax(arr)) # print the index of the maximum value