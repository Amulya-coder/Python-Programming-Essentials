# a Python program to calculate the difference between the two lists.
# list1 = [1, 3, 5, 7, 9]
# list2 = [1, 2, 4, 6, 7, 8]
# OUTPUT: [9, 3, 5, 8, 2, 4, 6]

list1 = [1, 3, 5, 7, 9]
list2 = [1, 2, 4, 6, 7, 8]

list3=[]

# Using loop
for ele in list1:
    if ele not in list2:
        list3.append(ele)
        
for ele in list2:
    if ele not in list1:
        list3.append(ele)
        
print(list3)