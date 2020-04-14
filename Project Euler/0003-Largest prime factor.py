
target = 600851475143

maxvalue = 0
def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

for i in range(2,target+1):
    if isPrime(i) and target % i == 0:
        maxvalue = i
        #print(i)
    if i > 1000000:
        break

print(maxvalue)