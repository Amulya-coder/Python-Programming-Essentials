# Anagram - contains same characters in any order

s1="listen"
s2="silent"

# Time comp:O(nlogn) space comp:O(1)
print(sorted(s1)==sorted(s2))

# Using list and append
l1=[]
l2=[]
s1='race'
s2='care'
for i in s1:
    l1.append(i.lower())
l1.sort()
for i in s2:
    l2.append(i.lower())
l2.sort()
if(l1==l2):
    print('Anagram')
else:
    print('Not anagram')