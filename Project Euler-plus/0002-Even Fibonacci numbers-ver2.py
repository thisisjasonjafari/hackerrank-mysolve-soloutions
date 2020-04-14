#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())


    a = 1
    b = 2
    counterO = 0
    counterO = counterO + b

    for i in range(1,n):
        c = a + b
        a = b
        b = c
        if c < n:
            if c % 2 == 0:
                counterO = counterO + c
        else:
            break
            
    print(  str(counterO))