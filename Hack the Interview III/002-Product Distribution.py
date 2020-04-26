'''

In this challenge, a string and a list of intervals are given. The string consists of English letters only and it can contain both lowercase and uppercase letters.

For two different letters, we say that the first letter is greater than the second letter when the first letter comes later in the alphabet than the second letter ignoring the case of the letters. For example, the letter 'Z' and 't' are greater than the letters 'b' and 'G', while the letters 'B' andd 'b' are equal as case is not considered.

The task is the following. For each given interval, you need to find the count of the greatest letter occurring in the string in that interval, ignoring the case of the letters, so occurrences of, for example,  and  are occurrences of the same letter.

Consider, for example, for the string "AbaBacD". In the interval, [0, 4], the greatest letter is 'b' with count 2.

Input Format

The first line contains integer , denoting the length of the input string.

The second line contains string .

The third line contains an integer , denoting the number of intervals. Each line of the  subsequent lines contains two space-separated integers  and , denoting the beginning and the end of  interval.

Constraints

Subtasks

For  of the maximum score.

Output Format

For each interval, print the count of the greatest letter occurring in the string in that interval.

Sample Input 0

5
ddaaa
1
0 4
Sample Output 0

2
Explanation 0

The string is "ddaaa" and there is only one interval, i.e. the interval  denoting the whole string. The greatest character occuring in that interval is  and its count is , therefore,  is the answer.

Sample Input 1

8
aAabBcba
5
2 6
1 2
2 2
0 4
0 7
Sample Output 1

1
2
1
2
1
Explanation 1

The input string is "aAabBcba" and there are 5 intervals to check:

 -> aA[abBcb]a -> '' is the greatest and occurs  time
 -> a[Aa]bBcba -> '' is the greatest and occurs  times
 -> aA[a]bBcba -> '' is the greatest and occurs  time
 -> [aAabB]cba -> '' is the greatest and occurs  times
 -> [aAabBcba] -> '' is the greatest and occurs  time'''


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
        h.sort()
        # if h[0] == h[1]:
        #     javab.append(0)
        #     continue
        first = h[0]
        last =   h[1]+1
        b = []
        for i in range(first , last):
            b.append(s[i].lower())
            
        print(b)
        b.sort(reverse = True)
        
        counter = 0
        for k in b:
            if k == b[0]:
                counter  = counter + 1
        javab.append(counter)
        
         
    
     
    
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

