# Python program to convert a given list of tuples to a list of lists.

"""
INPUT: [(1, 2), (2, 3), (3, 4)]
OUTPUT: [[1, 2], [2, 3], [3, 4]]
"""

t=[(1, 2), (2, 3), (3, 4)]
res=[list(ele) for ele in t]
print(res)
