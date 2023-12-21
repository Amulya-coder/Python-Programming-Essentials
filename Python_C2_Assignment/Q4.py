# Python program to print a specified list after removing the 0th, 4th and 5th element

a=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
b=[]
for i in a:
    if i not in ('Red', 'Pink', 'Yellow'):
        b.append(i)
        
print(b)