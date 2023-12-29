# Average of numbers in a list

l1=[1,2,3,4,5,6,7,8,9,10]

sum=0
for i in range(len(l1)):
    sum+=l1[i]
    print(i)
print(sum)
avg=sum/len(l1)
print(avg)