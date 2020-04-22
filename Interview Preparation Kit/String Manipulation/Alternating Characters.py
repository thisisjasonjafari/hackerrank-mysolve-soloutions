#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    pp = []
    counter = 0
    
    for i in s:
        if counter == 0:
            pp.append(i)
            counter =1
        if i == pp[len(pp)-1] :
            pass
        else :
            pp.append(i)
    #print(pp)   
    return (len(s) -len(pp))

    
s = "AAABBBABABAB"
alternatingCharacters(s)