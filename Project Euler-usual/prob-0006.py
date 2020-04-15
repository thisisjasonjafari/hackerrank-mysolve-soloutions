
'''
Euler Project 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''



n = 100

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

print(ervryvalPower2(n))
print(countAndPowe(n))

print(countAndPowe(n)-ervryvalPower2(n))