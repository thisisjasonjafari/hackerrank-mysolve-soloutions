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
    counter = 1
    counterchek =2
    while  True:
        if isPrime(counterchek):
            counter +=1        
        if(counter == n + 1):
                break
        counterchek+=1
    print(counterchek)