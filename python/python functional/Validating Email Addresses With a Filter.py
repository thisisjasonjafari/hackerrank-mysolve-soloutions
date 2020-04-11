import re

def fun(s):
   

    pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"

     
    valid_email = []
    kk = s.rstrip().split()
    for i in kk:
        if re.match(pattern,i) and i != "":
            valid_email.append(i)
            

    return ((valid_email))
    # return True if s is a valid email,