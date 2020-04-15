n=1000
product = -1
for a in range(1,int(n/3) +1):
    b = int((n * n - 2 * n * a)/(2 * n - 2 * a))
    c = n - a - b
    if (a * a + b * b) == (c * c):
        if a* b *c > product:
            product = a * b * c
print(int(product))
            