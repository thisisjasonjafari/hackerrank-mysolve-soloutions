n = int(input())
x =  (list(map(int, input().split())))
y =  (list(map(int, input().split())))
pp = []
for i in range ( 0 , len(x)):
    for j in range(0 , y[i]):
        pp.append(x[i])

from statistics import median
print(int(median(pp[:len(pp)//2])))
 
    #pp.append("orange")
