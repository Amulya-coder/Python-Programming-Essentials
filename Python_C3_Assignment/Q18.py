# Python function that takes a list of integers as input and returns the
# second largest element in the list.

l= [3, 5, 2, 8, 9, 5, 1]

largest=0
second_largest=0
for i in l:
    if i>largest:
        second_largest=largest
        largest=i
    elif second_largest<i:
        second_largest=i

print(second_largest)