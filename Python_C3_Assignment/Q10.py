#Python program that takes two lists as input and returns a new list
#containing the common elements between the two lists.

def intersection(l1,l2):
    
    # l3=[val for val in l1 if val in l2]
    # return l3
    
    # or 
    return list(set(l1) & set(l2))
    
    
l1 = [1, 2, 3, 4, 5]
l2 = [3, 4, 5, 6, 7]

print(intersection(l1,l2))
