'''
Python program to get a string made of the first 2 and last 2
characters of a given string. If the string length is less than 2, return the empty
string instead.
'''

s="w3resource"
if(len(s)<=2):
    print('')
temp="".join(s[:2])
res="".join(s[-2:])
print(temp+res)