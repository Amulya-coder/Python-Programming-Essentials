# Python program to create a list by concatenating a given list with a
# range from 1 to n.

l1=['p', 'q'] 
n=5

res=[]
for i in range(1,n+1):
    for j in l1:
        res.append(j+str(i))
        
print(res)