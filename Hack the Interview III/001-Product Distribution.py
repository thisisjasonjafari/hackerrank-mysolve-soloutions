'''
A company has requested to streamline their product allocation strategy, and given  products, each of which has an associated value, you are required to arrange these products into segments for processing. There are infinite segments indexed as 1, 2, 3 and so on.

However, there are two constraints:

You can assign a product to a segment with index  if and only if  or the segment with index  has at least  products.
Any segment must contain either no products or at least  products.
The score for a segment is defined as the index of the segment multiplied by the sum of values of the products it contains. The score of an arrangement of products is the sum of scores of segments. Your task is to compute the maximum score of an arrangement.

Consider, for example,  products and . One optimal way to assign is -

Assign the first three products to segment 1.
Assign the next three products to segment 2.
Assign the next five products to segment 3.
Note that we can not assign 2 products to segment 4 as the second constraint would be violated. The score of the above arrangement is -

1 * (1 + 2 + 3) + 2 * (4 + 5 + 6) + 3 * (7 + 8 + 9 + 10 + 11) = 6 + 30 + 135 = 171.

Since the arrangement score can be very large, print it modulo .

Input Format

In the first line, there are two space-separated integers  and .

In the second line, there are  space-separated integers  denoting the values associated with the products.

Constraints

Output Format

In a single line, print a single integer denoting the maximum score of the arrangement modulo .

Sample Input 0

5 2
1 5 4 2 3
Sample Output 0

27
Explanation 0

The array is  and . It is optimal to put the first and fourth products into the first segment and the remaining products to the second segment. Doing that, we get the arrangement score  which is the greatest score that can be obtained. Finally, the answer is  modulo  which is .

Sample Input 1

4 4
4 1 9 7 
Sample Output 1

21
Explanation 1

All the four products must be placed in the first segment. The score in this case will be 1 * (4 + 1 + 9 + 7) = 21.

'''






#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxScore' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER m
#


def maxScore(a, m):
    # a = [1,2,3,4,5,6,7,8,9,10,11]
    # m = 3
    b = a
    b.sort(reverse=True)
    baghimande = len(a)%m
    
    sumsum = 0
    if baghimande > 0 :
        for i in range(0,baghimande):
            sumsum += b[i]

    a.sort()
    counter = 0
    summmm = 0
    for i in range(0,len(a)-baghimande):
        if i%m == 0:
            counter +=1       
        summmm += a[i] * counter
        
    summmm += sumsum * counter
    mmm = 1000000007
    return (summmm%mmm)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    ans = maxScore(a, m)

    fptr.write(str(ans) + '\n')

    fptr.close()
