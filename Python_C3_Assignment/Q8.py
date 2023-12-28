# Python function to reverse a list at a specific location

'''
INPUT: [10,20,30,40,50,60,70,80]
start_pos = 2
end_pos = 4
OUTPUT: Reverse elements of the said list between index position 2 and 4
[10, 20, 50, 40, 30, 60, 70, 80]
'''

l=[10,20,30,40,50,60,70,80]
start_pos = 2
end_pos = 4
l1=l[:start_pos]
l2=l[start_pos:end_pos+1]
l3=l2[::-1]
l4=l[end_pos+1:]
print(l1+l3+l4)

# or using a while loop
def reverse(l,start_pos,end_pos):
    while start_pos<end_pos:
        l[start_pos],l[end_pos]=l[end_pos],l[start_pos]
        start_pos+=1
        end_pos-=1
    return l
        
l=[10,20,30,40,50,60,70,80]
print(reverse(l,2,4))