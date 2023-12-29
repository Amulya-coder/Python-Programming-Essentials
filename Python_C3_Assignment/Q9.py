'''
 Python program that takes a string as input and checks if it is a
palindrome (reads the same forwards and backward).
'''

s=input()
i=0
j=len(s)-1
flag=1
while i<j:
    i+=1
    j-=1
    if s[i]==s[j]:
        continue
    else:
        print("false")
        flag=0
        break
    
if flag:
    print('true')