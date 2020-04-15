    #!/bin/python3

import sys




def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True




t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sum = 0
    for i in range(2,n+1):
        if isPrime(i):
            sum += i

    print(sum)

