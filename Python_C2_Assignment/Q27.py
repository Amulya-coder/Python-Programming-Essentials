# Python function to reverse a string if its length is a multiple of 4.

def reverse(s):
    n=len(s)
    if n%4==0:
        return "".join(s[::-1])
        
    return s

print(reverse("Hell"))
print(reverse("Hello"))