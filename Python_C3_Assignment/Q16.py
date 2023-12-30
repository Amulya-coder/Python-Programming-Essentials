#  Python function that accepts a string and counts the number of upperand lower-case letters.

def string(s):
    
    d={'Uppercase':0,'lowercase':0}
    
    for i in s:
        if i.isupper():
            d['Uppercase']+=1
        elif i.islower():
            d['lowercase']+=1
            
    return d