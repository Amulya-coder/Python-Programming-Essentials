# Write a Pandas program to add, subtract, multiple and divide two Pandas Series.
# Input: [2, 4, 6, 8, 10], [1,3,5,7,9]

ds1 = pd.Series([2, 4, 6, 8, 10])
ds2 = pd.Series([1, 3, 5, 7, 9])
ds = ds1 + ds2
s2=  ds1-ds2
s3= ds1*ds2
s4= ds1/ds2
