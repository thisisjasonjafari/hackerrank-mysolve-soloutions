
'''
Euler Project 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''


def checkForTrue(target):
    for i in range(1,21):
        if target % i != 0 :
            return False
        
    return True


counter = 1
while True:
    if checkForTrue(counter) == True:
        print(counter)
        break
    else:
        counter += 1