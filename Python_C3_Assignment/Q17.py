# Python function to check whether a number falls within a given
# range(3,9)

def lies(n,start,end):
    if n in range(start,end):
        print(n,'Lies in range')
    else:
        print(n,"doesn't lies in range")

lies(5,3,9)