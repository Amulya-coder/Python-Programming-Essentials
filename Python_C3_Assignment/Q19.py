'''
Python lambda function that takes a list of numbers and an exponent n
as input and returns a new list with each element raised to the power of n.
'''

'''
INPUT:
input_numbers = [1, 2, 3, 4, 5]
exponent = 3
OUTPUT: [1, 16, 81, 256, 625]
'''

l=[1,2,3,4,5]
n=3

#(lambda x,y: x+y)
#USING LIST COMPREHENSION
ans=[num**n for num in l]
print(ans)

#Using lambda and map
res=list(map(lambda x:x**n,l))
print(res)