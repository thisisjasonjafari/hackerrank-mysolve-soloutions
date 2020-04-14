#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    first = 0
    second = 1 
    summ= 0
    sumeven = 0

    while second <= n:
        summ =first + second
        first= second
        second = summ
        if(summ%2 == 0 and summ <n):
            sumeven += summ
    print(sumeven)    
        
    
