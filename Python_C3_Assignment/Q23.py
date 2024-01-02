# Python program to check the validity of passwords input by users.

import re

def checkPassword(password):
    
    if len(password)<6 and len(password)>16:
        return False
    if not re.search("[a-z]",password):
        return False
    if not re.search("[A-Z]",password):
        return False
    if not re.search("[$#@]",password):
        return False
    
    return True
        
password="S3r@100a"

if checkPassword(password):
    print("Valid password")
else:
    print("Invalid Password")



