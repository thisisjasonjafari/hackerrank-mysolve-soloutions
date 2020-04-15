from operator import mul
import sys
from functools import reduce

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    numList = [int(x) for x in str(num)]
    prod = []
    for i in range(0,len(numList)-k):
        prod.append(reduce(mul,numList[i:i+k]))
    print(max(prod))