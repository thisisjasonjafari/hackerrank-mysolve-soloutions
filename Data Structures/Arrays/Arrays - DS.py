#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the reverseArray function below.



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    mas = []
    for i in range(len(arr)-1, -1, -1):
        mas.append(arr[i])

    fptr.write(' '.join(map(str, mas)))
    fptr.write('\n')

    fptr.close()
