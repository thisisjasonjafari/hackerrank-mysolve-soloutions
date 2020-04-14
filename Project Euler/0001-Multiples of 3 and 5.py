#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sumDigit = 0
    for i in range(1,n):
        if i % 5 == 0 or i % 3 == 0:
            sumDigit += i
            
    print(sumDigit)
