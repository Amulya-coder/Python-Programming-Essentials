# Python program that prints each item and its corresponding type from
# the following list.

'''
INPUT = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V',
"section":'A'}]
OUTPUT:
Type of 1452 is <class 'int'>
Type of 11.23 is <class 'float'>
Type of (1+2j) is <class 'complex'>
Type of True is <class 'bool'>
Type of w3resource is <class 'str'>
'''

list=[1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V',"section":'A'}]
n=len(list)
print(n)
for i in range(n):
    print('Type of ',list[i],'is ',type(list[i]))