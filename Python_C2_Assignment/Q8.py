# find the frequency of each element in a list

a= [1, 2, 3, 2, 4, 1, 3, 5, 2, 3, 4, 1]

dict={}
for i in a:
    dict[i]=a.count(i)
    
print(dict) # output: {1: 3, 2: 3, 3: 3, 4: 2, 5: 1}

# count function returns the count of an element
# x=a.count(1) #3