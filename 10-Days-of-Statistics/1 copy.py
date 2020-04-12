arr = [1,1,1,1,15,3,3,3,9,3,3,3]

def compress_array(arr):
    s=-100    
    counter = 0 
    value= 0
    arrg=[]
    for i in arr:
        
        if i != s :
            s=i
            if value !=0:
                arrg.append(value)
                arrg.append(counter)
            counter = 1
            value=i
        elif i == s:
            counter = counter +1 
        
        

         
    print(arrg)

compress_array(arr)
    # Enter your code here