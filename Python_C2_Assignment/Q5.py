# a Python program to print the numbers of a specified list after removing
# even numbers from it

a= [7,8, 120, 25, 44, 20, 27]
b=[]

for num in a:
    if num%2!=0 :
        b.append(num)
        
print(b)