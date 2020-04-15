def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


n = 5

sum = 0
for i in range(2,n):
    if isPrime(i):
        sum += i

print(sum)
