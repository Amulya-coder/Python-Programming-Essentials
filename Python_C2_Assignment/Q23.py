# Python program to count the number of characters (character
# frequency) in a string.

s="google.com"
dict={}
for i in s:
    dict[i]=s.count(i)
    
print(dict)