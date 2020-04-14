
#!/bin/python3

# https://www.hackerrank.com/challenges/plus-minus/problem


import math
import os
import random
import re
import sys


# Complete the plusMinus function below.
def plusMinus(arr):
    countPosetive = 0
    countNegative = 0
    countZero = 0
    for i in arr:
        if int(i) > 0:
            countPosetive += 1
        elif int(i) == 0:
            countZero += 1
        else:
            countNegative += 1

    ratioPos = (countPosetive / (len(arr)))
    ratioNeg = (countNegative / (len(arr)))
    ratioZer = (countZero / (len(arr)))
    print("%.6f" % ratioPos)
    print("%.6f" % ratioNeg)
    print("%.6f" % ratioZer)
     


if __name__ == '__main__':
    #n = int(input())
    n = 6
    ss = "-4 3 -9 0 4 1"
    #arr = list(map(int, input().rstrip().split()))
    arr = list(map(int, ss.rstrip().split()))

    plusMinus(arr)
