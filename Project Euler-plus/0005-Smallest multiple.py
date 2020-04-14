#!/bin/python3

import sys


 

def checkForTrue(target , h):
    for i in range(1,h + 1):
        if target % i != 0 :
            return False
        
    return True





t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    counter = n + 1
    s =0
    while s == 0:
        if checkForTrue(counter ,n) == True:
            print(counter)
            break
        else:
            counter += 1


