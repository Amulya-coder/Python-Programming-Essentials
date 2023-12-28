# Python program to get the Fibonacci series between 0 and 50.

first=0
second=1
for i in range(0,50):
    if i<=1:
        next=i
    else:
        next=first+second
        first=second
        second=next
    print(next)