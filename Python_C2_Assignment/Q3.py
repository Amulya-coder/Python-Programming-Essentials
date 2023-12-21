# a Python program to count the number of strings from a given list of
# strings with length 2 or more and the first and last characters are the same.

a= ['abc', 'xyz', 'aba', '1221']
count=0
for s in a:
    if len(s)>=2 and s[0]==s[-1]:
        count+=1
print(count)