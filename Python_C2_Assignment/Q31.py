#  Python program to count and display vowels in text.

a='resource'
count=0
list=[]
for i in a:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        count+=1
        list.append(i)

print(f'{count} -> {list}')