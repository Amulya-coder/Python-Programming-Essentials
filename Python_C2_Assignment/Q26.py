# Python program to count the occurrences of each word in a given
# sentence.

'''
INPUT: ‘the quick brown fox jumps over the lazy dog.’
OUTPUT: {'the': 2, 'jumps': 1, 'brown': 1, 'lazy': 1, 'fox': 1, 'over': 1, 'quick': 1,
'dog.': 1}
'''

s='the quick brown fox jumps over the lazy dog.'
res=s.split(' ')
dict={}

for i in res:
    dict[i]=res.count(i)
    
print(dict)