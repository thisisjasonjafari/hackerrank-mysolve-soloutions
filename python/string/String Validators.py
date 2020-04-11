if __name__ == '__main__':
    s = str(input())
     
    v= False
    for j in s:
        if  j.isalnum():
            v=True
    print(v) 
    v= False
    for j in s:
        if  j.isalpha():
            v=True
    print(v) 
    v= False
    for j in s:
        if  j.isdigit():
            v=True
    print(v) 
        
    for j in s:
        if  j.islower():
            v=True
    print(v) 
        
    for j in s:
        if  j.isupper():
            v=True
    print(v) 
        

    
