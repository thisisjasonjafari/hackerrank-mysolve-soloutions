#!/bin/python3

import math
import os
import random
import re
import sys

n = int(input())
d = {}
for i in range(n):
    x = input().split()
    d[x[0]] = x[1]
while True:
    try:
        name = input()
        if name in d:
            print(name, "=", d[name], sep="")
        else:
            print("Not found")
    except:
        break
