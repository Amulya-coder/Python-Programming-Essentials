# Python program to check if a set is a subset of another set.

"""
INPUT:
x: {'mango', 'apple'}
y: {'mango', 'orange'}
z: {'mango'}
OUTPUT:
If x is subset of y:False
If y is subset of z:False
"""

x= {'mango', 'apple'}
y= {'mango', 'orange'}
z= {'mango'}

print(z.issubset(y)) # True