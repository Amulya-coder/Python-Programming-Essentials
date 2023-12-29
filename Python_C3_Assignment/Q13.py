# Convert a list of duplicates into a unique list

n = int(input("Enter number of elements : "))
l1=[] 

for i in range(0, n):
    ele = int(input())
    l1.append(ele) 
    
l2=[]

for i in range(len(l1)):
    if l1[i] not in l2:
        l2.append(l1[i])
print(l2)

l3=set(l1)
print(list(l3))