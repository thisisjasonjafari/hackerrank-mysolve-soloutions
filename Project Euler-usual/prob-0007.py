
def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

n =10001
counter = 1
counterchek =2
while  True:
    if isPrime(counterchek):
        counter +=1        
    if(counter == n + 1):
            break
    counterchek+=1


print(counterchek)