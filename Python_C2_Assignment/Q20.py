# Python program to check if two given sets have no elements in common

# Using for loop
def compare_set():
    s1={1, 2, 3, 4}
    s2={4, 5, 6, 7}
    
    for i in s1:
        if i in s2:
            return True
    return False
            
print(compare_set())