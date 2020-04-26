#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMaxCharCount' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. 2D_INTEGER_ARRAY queries
#
def getMaxCharCount(s, queries):
    javab = []
    for h in queries:
        if h[0] == h[1]:
            javab.append(1)
            continue            
        v = s[h[0] : h[1]+1]
        if len(v) ==1:
            javab.append(1)
            continue 
        v = v.lower()
        u = list(set(v))
        u.sort()
        count = v.count(u[len(u)-1])
        javab.append(count)         
    return javab

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    q = int(input().strip())

    query = []

    for _ in range(q):
        query.append(list(map(int, input().rstrip().split())))

    ans = getMaxCharCount(s, query)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
