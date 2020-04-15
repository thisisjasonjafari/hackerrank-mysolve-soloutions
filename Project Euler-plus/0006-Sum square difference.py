#!/bin/python3

import sys

def ervryvalPower2(n):
    counterrr = 0
    for i in range(1,1+n):
        counterrr += i * i
    return counterrr

def countAndPowe(n):
    counterrr = 0
    for i in range(1,1+n):
        counterrr += i 
    return counterrr * counterrr


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())    
    print(countAndPowe(n)-ervryvalPower2(n))
