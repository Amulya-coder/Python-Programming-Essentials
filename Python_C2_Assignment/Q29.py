#  Python program to reverse words in a string

s="The quick brown fox jumps over the lazy dog"
reverse=s.split(' ') # split into separate elements in form of list
temp=" ".join(reversed(reverse))
print(temp)