# Python program to convert a list of multiple integers into a single integer

l1= [11, 33, 50]

res=""
for i in l1:
    res+=str(i)

print(int(res))

num=int(res) #convert string to int
print(type(num)) # To check datatype of variable